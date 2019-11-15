source 3_data.sql;
--
-- NOT - !=
SELECT
  title,
  released_year
FROM books
WHERE
  released_year != 2017;
--
  -- NOT LIKE
SELECT
  title
FROM books
WHERE
  title NOT LIKE '%W%';
--
  -- GREATER - >
SELECT
  *
FROM books
WHERE
  released_year > 2005;
--
  -- TRUE = 1, FALSE = 0
SELECT
  99 > 1;
-- > 1
SELECT
  "A" = "a";
-- > 1
SELECT
  "a" > "b";
-- > 0
  --
  -- LOGICAL - AND / &&
  -- LOGICAL - OR / ||
SELECT
  released_year
FROM books
WHERE
  released_year > 2005
  AND released_year < 2013;
--
  -- BETWEEN
SELECT
  released_year
FROM books
WHERE
  released_year BETWEEN 2010
  AND 2012;
-- inclusive the intervalls!
  --
  -- NOT BETWEEN
SELECT
  pages
FROM books
WHERE
  pages NOT BETWEEN 200
  AND 1000;
--
  -- Comparing dates use CAST
SELECT
  CAST('2000-01-01' AS DATETIME);
--
  -- IN / NOT IN
SELECT
  title,
  author_lname
FROM books
WHERE
  author_lname IN ("Carver", "Lahiri", "Smith");
--
SELECT
  released_year
FROM books
WHERE
  released_year NOT IN (2000, 2002);
--
  -- Modulo / %
SELECT
  released_year
FROM books
WHERE
  released_year % 2 != 0;
--
  --
  -- CASE
SELECT
  author_lname,
  released_year,
  CASE
    WHEN released_year >= 2000 THEN 'Modern Lit'
    ELSE '20th Century Lit'
  END AS Genre
FROM books;
--
SELECT
  title,
  CASE
    WHEN stock_quantity <= 50 THEN '*'
    WHEN stock_quantity BETWEEN 51
    AND 100 THEN '**'
    ELSE '***'
  END AS Stock
FROM books;