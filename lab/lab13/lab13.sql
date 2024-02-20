.read data.sql

CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = "blue" AND pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = "blue" AND pet = "dog";


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b 
  WHERE a.pet = b.pet AND a.song = b.song AND a.time < b.time 
  ORDER BY a.time;


CREATE TABLE sevens AS
  SELECT s.seven FROM students AS s, numbers AS n
  WHERE s.number = 7 AND n."7" = "True" AND s.time = n.time;

CREATE TABLE favpets AS
  SELECT pet, count(*) AS count FROM students
  GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE dog AS
  SELECT pet, count(*) AS count FROM students
  WHERE pet = "dog";

CREATE TABLE bluedog_agg AS
  SELECT song, count(*) AS count FROM bluedog_songs
  GROUP BY song ORDER BY count DESC;


CREATE TABLE instructor_obedience AS
  SELECT seven, instructor, count(*) AS count FROM students 
  WHERE seven = '7' GROUP BY instructor ORDER BY instructor;