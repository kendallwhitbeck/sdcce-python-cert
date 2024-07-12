UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

INSERT INTO movies_info_1
VALUES (1, 'Action/Sci-fi', 'Star Wars: Episode III - Revenge of the Sith', 'George Lucas');

SELECT m1.genre AS Genre, m1.title AS Title, m1.director AS Director, m2.release_year AS Year, m2.description AS Description
FROM movies_info_1 AS m1 JOIN movies_info_2 AS m2 ON m1.show_id = m2.show_id;

DELETE FROM table_name WHERE condition;

SELECT m.name as Title, m.year as Year, m.minutes as Length, c.name as Genre FROM Movie as m JOIN Category as c ON m.categoryID = c.categoryID WHERE year = 2002
SELECT m.name as Title, m.year as Year, m.minutes as Length, c.name as Genre
FROM Movie as m JOIN Category as c ON m.categoryID = c.categoryID
WHERE year = 2002;