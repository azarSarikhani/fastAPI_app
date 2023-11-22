CREATE TABLE shopdb.animals (
     id MEDIUMINT NOT NULL AUTO_INCREMENT,
     name CHAR(30) NOT NULL,
     PRIMARY KEY (id)
);

INSERT INTO animals (name) VALUES
    ('dog'),('cat'),('penguin'),
    ('lax'),('whale'),('ostrich');

SELECT * FROM animals;

CREATE USER 'fastpi_user' IDENTIFIED BY 'fastapi_pass';

GRANT ALL PRIVILEGES ON shopdb.animals TO 'fastpi_user';
