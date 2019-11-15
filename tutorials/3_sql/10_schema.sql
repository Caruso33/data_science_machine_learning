DROP DATABASE sql_course_web_app;
--
CREATE DATABASE sql_course_web_app;
--
USE sql_course_web_app;
--
CREATE TABLE users(
  email VARCHAR(255) PRIMARY KEY,
  created_at TIMESTAMP DEFAULT NOW()
)