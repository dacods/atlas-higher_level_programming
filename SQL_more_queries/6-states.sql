-- Creates a database and a table in MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
)