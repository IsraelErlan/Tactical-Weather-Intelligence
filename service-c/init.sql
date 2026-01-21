CREATE DATABASE IF NOT EXISTS weather_db;
USE weather_db;

CREATE TABLE IF IS NOT EXISTS weather_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    location_name VARCHAR(100),
    country VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT,
    temperature FLOAT,
    wind_speed FLOAT,
    humidity INT,
    temperature_category VARCHAR(50),
    wind_category VARCHAR(50)
);
