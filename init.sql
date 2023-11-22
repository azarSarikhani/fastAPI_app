CREATE TABLE shopdb.animals (
     id MEDIUMINT NOT NULL AUTO_INCREMENT,
     name CHAR(30) NOT NULL,
     PRIMARY KEY (id)
);

INSERT INTO animals (name) VALUES
    ('dog'),('cat'),('penguin'),
    ('lax'),('whale'),('ostrich');

SELECT * FROM animals;

CREATE USER 'fastpi'@'127.0.0.1' IDENTIFIED BY 'fastapipass';

GRANT ALL PRIVILEGES ON shopdb.animals TO 'fastpi'@'127.0.0.1';