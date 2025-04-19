CREATE DATABASE todo_db;
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON todo_db.* TO 'username'@'localhost';
FLUSH PRIVILEGES;