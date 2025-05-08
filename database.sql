-- Criação das tabelas
CREATE TABLE Departamento (
    id_departamento SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    localizacao VARCHAR(100),
    orcamento DECIMAL(15,2)
);

CREATE TABLE if not exists Funcionario (
    id_funcionario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    salario DECIMAL(10,2),
    data_contratacao DATE,
    id_departamento INTEGER REFERENCES Departamento(id_departamento)
);

CREATE TABLE if not exists Projeto (
    id_projeto SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    data_inicio DATE,
    data_termino DATE,
    orcamento DECIMAL(15,2),
    id_departamento_responsavel INTEGER REFERENCES Departamento(id_departamento)
);

-- Inserções na tabela Departamento
INSERT INTO if not exists Departamento (nome, localizacao, orcamento) 
VALUES
('TI', 'Andar 5', 500000.00),
('RH', 'Andar 2', 200000.00),
('Financeiro', 'Andar 3', 350000.00),
('Marketing', 'Andar 4', 300000.00),
('Vendas', 'Andar 1', 450000.00),
('Produção', 'Andar 0', 600000.00),
('Jurídico', 'Andar 2', 150000.00),
('Logística', 'Andar -1', 250000.00),
('Pesquisa', 'Andar 6', 400000.00),
('Qualidade', 'Andar 0', 180000.00);

-- Inserções na tabela Funcionario
INSERT INTO Funcionario (nome, cargo, salario, data_contratacao, id_departamento)
 VALUES
('João Silva', 'Desenvolvedor', 7500.00, '2020-05-15', 1),
('Maria Santos', 'Gerente de RH', 9500.00, '2018-03-10', 2),
('Carlos Oliveira', 'Analista Financeiro', 6500.00, '2021-01-20', 3),
('Ana Pereira', 'Designer', 5500.00, '2022-06-05', 4),
('Pedro Costa', 'Vendedor', 5000.00, '2021-11-15', 5),
('Luiza Almeida', 'Engenheira de Produção', 8500.00, '2019-09-03', 6),
('Fernando Souza', 'Advogado', 9000.00, '2020-07-22', 7),
('Juliana Lima', 'Coordenadora de Logística', 7000.00, '2021-04-18', 8),
('Ricardo Martins', 'Pesquisador', 8000.00, '2018-12-01', 9),
('Patrícia Rocha', 'Analista de Qualidade', 6000.00, '2022-02-14', 10);

-- Inserções na tabela Projeto
INSERT INTO Projeto (nome, descricao, data_inicio, data_termino, orcamento, id_departamento_responsavel) 
VALUES
('Sistema ERP', 'Implementação de novo sistema integrado', '2023-01-10', '2023-12-15', 250000.00, 1),
('Treinamento Corporativo', 'Programa de capacitação para funcionários', '2023-03-01', '2023-06-30', 50000.00, 2),
('Otimização de Custos', 'Análise e redução de despesas', '2023-02-15', '2023-09-30', 80000.00, 3),
('Campanha Verão', 'Lançamento de nova linha de produtos', '2023-04-01', '2023-08-31', 120000.00, 4),
('Expansão de Mercado', 'Abertura de novas filiais', '2023-05-01', '2024-05-01', 300000.00, 5),
('Automação Industrial', 'Modernização das linhas de produção', '2023-06-15', '2024-06-14', 450000.00, 6),
('Conformidade Legal', 'Adequação às novas leis trabalhistas', '2023-01-20', '2023-07-20', 60000.00, 7),
('Sistema de Rastreamento', 'Implementação de GPS em frota', '2023-03-15', '2023-10-31', 90000.00, 8),
('Novo Produto X', 'Pesquisa e desenvolvimento de novo item', '2023-02-01', '2024-02-01', 200000.00, 9),
('ISO 9001', 'Certificação de qualidade', '2023-01-05', '2023-11-30', 75000.00, 10);
