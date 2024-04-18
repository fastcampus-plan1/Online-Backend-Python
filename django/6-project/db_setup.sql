CREATE DATABASE IF NOT EXISTS `restaurant_db`;
CREATE USER IF NOT EXISTS 'restaurant_user'@'%' IDENTIFIED BY 'db_password';
GRANT ALL PRIVILEGES ON `restaurant_db`.* TO 'restaurant_user'@'%';
FLUSH PRIVILEGES;
