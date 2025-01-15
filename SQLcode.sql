Create database db;
SET sql_mode = "";

use db

Create table movies(
movieid int,
title varchar(255),
genre varchar(255));

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/movies.csv' 
INTO TABLE movies
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
ignore 1 rows;

Create table ratings(
userid int,
movieid int,
rating float,
timestamp float);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ratings.csv' 
INTO TABLE ratings
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
ignore 1 rows;

SELECT COUNT(*) AS movie_count FROM movies;

SELECT *
FROM movies
WHERE genre LIKE '%Action%';

SELECT *
FROM movies
WHERE title Like '%2000%';
