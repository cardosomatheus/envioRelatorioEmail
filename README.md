# envioRelatorioEmail
Este projeto automatiza a extração de dados de um banco PostgreSQL, transforma os resultados em arquivos CSV, compacta e envia por email para os destinatários configurados.

Funcionalidades
Conexão com banco de dados PostgreSQL usando SQLAlchemy

Execução de consultas SQL e transformação em DataFrames com Pandas

Geração de arquivos CSV a partir dos resultados

Compactação dos arquivos em formato ZIP

Envio automático por email com anexo ZIP


# Configuração
1- Clone o repositório:
git clone https://github.com/cardosomatheus/envioRelatorioEmail.git

2- Instale as dependências:
pip install -r requirements.txt

3- Configure as variáveis de ambiente no arquivo .env:

4- Execute o arquivo "database.sql" em seu banco de dados postgresql

5-Configure os destinatários no arquivo config.py

6 - Execute o arquivo "main.py"

