CREATE DATABASE IF NOT EXISTS zak_db;
USE zak_db;

CREATE TABLE Zak (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    vRabote TINYINT(1) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Zak (name, vRabote) VALUES 
('zakaz1', 1),
('zakaz2', 0),
('zakaz3', 1),
('zakaz4', 1),
('zakaz5', 0);


drop DATABASE zak_db;