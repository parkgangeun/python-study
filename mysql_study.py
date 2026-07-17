CREATE DATABASE my_study;
USE my_study;
CREATE TABLE drivers (name VARCHAR(50), team VARCHAR(50),lap_time INT);
INSERT INTO drivers VALUES ('Hamilton', 'Mercedes', 90);
INSERT INTO drivers VALUES ('Verstappen', 'Red Bull', 85);
INSERT INTO drivers VALUES ('Leclerc', 'Ferrari', 92);
INSERT INTO drivers VALUES ('Norris', 'McLaren', 95);
INSERT INTO drivers VALUES ('Alonso', 'Aston Martin', 98);
SELECT * FROM drivers WHERE team = 'Red Bull';⁠
SELECT name, lap_time FROM drivers ORDER BY lap_time ASC LIMIT 3;⁠
SELECT * FROM drivers;
SELECT * FROM drivers ORDER BY lap_time ASC;⁠