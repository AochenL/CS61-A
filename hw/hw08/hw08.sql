CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name, s.size FROM dogs AS d, sizes AS s
  WHERE d.height > s.min AND d.height <= s.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT d2.name FROM dogs AS d1, dogs AS d2, parents AS p
  WHERE d1.name = p.parent AND d2.name = p.child ORDER BY d1.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT p1.child AS sib1, p2.child AS sib2 FROM parents AS p1, parents AS p2
  WHERE p1.child < p2.child AND p1.parent = p2.parent ORDER BY sib1;


-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT s.sib1 || " and " || s.sib2 || " are "  || size_of1.size || " siblings"
  FROM siblings AS s, size_of_dogs AS size_of1, size_of_dogs AS size_of2
  WHERE s.sib1 = size_of1.name AND s.sib2 = size_of2.name AND size_of1.size = size_of2.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height


-- Add your INSERT INTOs here


CREATE TABLE my_stacks_helper AS
SELECT s1.name AS d1, s1.height AS h1, 
       s2.name AS d2, s2.height AS h2, 
       s3.name AS d3, s3.height AS h3, 
       s4.name AS d4, s4.height AS h4,
       s1.height + s2.height + s3.height + s4.height as total_height
FROM dogs AS s1, dogs AS s2, dogs AS s3, dogs AS s4
WHERE s1.height < s2.height AND s2.height < s3.height AND s3.height < s4.height
AND s1.height + s2.height + s3.height + s4.height > 170
ORDER BY total_height;


CREATE TABLE stacks AS
  SELECT d1 || ", " || d2 || ", " || d3 || ", " || d4 AS names, total_height FROM my_stacks_helper;

