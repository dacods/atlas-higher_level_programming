-- Creates a database and a table in MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO PRIMARY,
    name VARCHAR(256)
)