﻿#libs
import smtplib
import os
from sqlalchemy import create_engine,engine
from pandas import read_sql_query
from shutil import rmtree, make_archive
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

query_dict = {
    "projetos":"""select A.nome,
                        A.descricao,
                        A.orcamento,
                        to_char(data_inicio,'DD/MM/YYYY') as DATA_INICIO,
                        to_char(data_termino ,'DD/MM/YYYY') as DATA_TERMINO,
                        data_termino::date- data_inicio::date as qtd_dias
                        from public.projeto A""",
                        
    "funcionarios":"""SELECT A.NOME AS NOME_FUNCIONARIO,
                             A.CARGO,
                             B.NOME AS NOME_DEPARTAMENTO,
                             B.LOCALIZACAO,
                             C.NOME AS NOME_PROJETO,
                             C.DESCRICAO
                        FROM FUNCIONARIO A
                        JOIN DEPARTAMENTO B ON A.id_departamento  = B.id_departamento
                        JOIN PROJETO C ON A.id_departamento = C.id_departamento_responsavel;
                    """
}


# Variáveis no escopo global
load_dotenv()
DB_USUARIO = os.getenv("USER")
DB_SENHA   = os.getenv("PWD")
DATABASE   = os.getenv("DATABASE")
DB_HOST    = os.getenv("HOST")
DB_PORT    = os.getenv("PORT")

REMETENTE_EMAIL =  os.getenv("REMETENTE")
REMETENTE_PORTA = os.getenv("REMETENTE_PORTA")
REMETENTE_SENHA = os.getenv("REMETENTE_SENHA")

assunto_email = 'Relatorios semanais'
pasta_relatorio = 'relatoriosEmail'




def conexao_db_postgres():
    string = f"postgresql+psycopg2://{DB_USUARIO}:{DB_SENHA}@{DB_HOST}/{DATABASE}"
    return create_engine(string)


def cria_pasta_relatorio(pasta_relatorio:str = pasta_relatorio) -> None:
    # Deleta a pasta de relatoriosOiSemanal caso exista.
    if pasta_relatorio in os.listdir():
        try:
            rmtree(os.path.join(os.getcwd(), pasta_relatorio))
        except OSError as e:
            print(f"Erro ao deletar a pasta de relatorio:  {e.filename} - {e.strerror}")
    
    # Cria a pasta de relatoriosOiSemanal novamente.
    os.mkdir(pasta_relatorio)


def arquivos_csv_zipados(pasta_relatorio:str = pasta_relatorio) -> None:
    global corpo_email
    corpo_email = """Prezados, bom dia.\nSegue em anexo Os relatorios semanais.\n\n"""

    # conexao com o bd
    engine = conexao_db_postgres()

    # Cria um csv para Query no dicionario (query_dict)
    for key, value in query_dict.items():
        df = read_sql_query(sql=value, con=engine)
        
        corpo_email += f'{key.upper()} possui {df.shape[0]} linhas.\n'
        df.to_csv(f'{pasta_relatorio}/{key}.csv',index=False)
    
    corpo_email += "\n\n Atencionsamente; \n\n"
    
   # Zipa a pasta de relatorios
    make_archive(pasta_relatorio, 'zip', pasta_relatorio)


def enviar_email(dict_remetente: dict, destinatarios: list, assunto: str, corpo_mensagem: str,pasta_relatorio:str = pasta_relatorio) -> None:
    """summary
    Args:
        destinatarios (list): recebedores do email.
        assunto (str): assunto do email
        corpo_mensagem (str): mensagem interna do email.
        
    """
    smtp_server = 'smtp.gmail.com'
    remetente   = dict_remetente.get('remetente')
    porta       = dict_remetente.get('poste')
    senha_app   = dict_remetente.get('senha')
    
    print('==== Iniciando o envio de email.!!!! ====\n')
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To']   = ','.join(destinatarios)
    mensagem['subject'] = assunto
    mensagem.attach(MIMEText(corpo_mensagem,'plain'))

    print(f'==== Anexando a pasta {pasta_relatorio}.zip !!!!  ====\n')
    with open(pasta_relatorio+'.zip', 'rb') as file:
        mensagem.attach(MIMEApplication(file.read(), Name=f'{pasta_relatorio}.zip'))
    
    try:
        server = smtplib.SMTP(smtp_server,porta)
        server.starttls()
        server.login(remetente,senha_app)
        server.sendmail(remetente,destinatarios, mensagem.as_string())
        print('==== email enviado com sucesso. !!!! ====\n')
        
    except Exception as e:
        print(f'Error no envio de email. {e}')
    
    finally:
        server.quit()




def main():
    print("======================  Iniciando Pipeline de envio de email.  ======================\n" )
    cria_pasta_relatorio(pasta_relatorio=pasta_relatorio)
    arquivos_csv_zipados(pasta_relatorio=pasta_relatorio)
    enviar_email(dict_remetente= {
                                    'remetente':REMETENTE_EMAIL,
                                    'porta':REMETENTE_PORTA,
                                    'senha':REMETENTE_SENHA
                                },
                 destinatarios=[
                                    'email_exemplo1@gmail.com',
                                    'email_exemplo1@gmail.com'
                                ],
                 assunto=assunto_email,
                 corpo_mensagem=corpo_email,
                 pasta_relatorio=pasta_relatorio)
    print("======================  Pipeline finalizada.  ======================\n" )



if __name__ == '__main__':
    main()
