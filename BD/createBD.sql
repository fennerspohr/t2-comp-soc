CREATE TABLE IF NOT EXISTS inventariante (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    senha VARCHAR(100),
    email VARCHAR(100),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
);

CREATE TABLE IF NOT EXISTS unidade (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
);

CREATE TABLE IF NOT EXISTS departamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    id_unidade INT NOT NULL,
    FOREIGN KEY (id_unidade) REFERENCES unidade(id)
);

CREATE TABLE IF NOT EXISTS sala (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    id_departamento INT NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id)
);

CREATE TABLE IF NOT EXISTS item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descr VARCHAR(500) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    valor DECIMAL(10,2),
    data_aquisicao DATETIME,
    foto_bem LONGBLOB NOT NULL,
    qrcode VARCHAR(100) NOT NULL,
    observacao VARCHAR(500),
    estado_fisico VARCHAR(50),
    condicao_uso VARCHAR(50),
    conservacao VARCHAR(50),
    funcionalidade VARCHAR(50),
    id_unidade INT NOT NULL,
    id_departamento INT NOT NULL,
    id_sala INT NOT NULL,
    FOREIGN KEY (id_unidade) REFERENCES unidade(id),
    FOREIGN KEY (id_departamento) REFERENCES departamento(id),
    FOREIGN KEY (id_sala) REFERENCES sala(id)
);

CREATE TABLE IF NOT EXISTS vistoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_hora_ini DATETIME,
    data_hora_fim DATETIME,
    foto_ini LONGBLOB,
    foto_fim LONGBLOB,
    id_inventariante INT NOT NULL,
    id_sala INT NOT NULL,
    FOREIGN KEY (id_inventariante) REFERENCES inventariante(id),
    FOREIGN KEY (id_sala) REFERENCES sala(id)
);

