-- Creates a table on MySQL server
CREATE TABLE IF NOT EXISTS unique_id (
    id UNIQUE DEFAULT 1,
    name VARCHAR(256)
)