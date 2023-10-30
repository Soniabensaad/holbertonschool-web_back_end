-- create table
create table IF NOT EXISTS users (
    id INT  NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name  NOT NULL VARCHAR(255),
    email VARCHAR(255) NOT NULL UNIQUE,
    
)
