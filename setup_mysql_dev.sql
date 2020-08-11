# script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

USE hbnb_dev_db;

CREATE USER IF NOT EXISTS ‘hbnb_dev’@'localhost' IDENTIFIED BY 'hbnt_dev_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev' @'hbnb_dev_db';

GRANT
SELECT
    ON performance_schema.* TO 'hbnb_dev' @'hbnb_dev_db';