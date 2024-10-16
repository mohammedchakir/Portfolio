-- Create a new database for the portfolio
CREATE DATABASE IF NOT EXISTS portfolio_db;

-- Use the newly created database
USE portfolio_db;

-- Create a table to store user information
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Example of inserting a user (remove this after testing)
-- INSERT INTO users (name, email, message) VALUES ('John Doe', 'john@example.com', 'This is a test message');