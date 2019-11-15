source 3_data.sql;
--
--
-- unique
SELECT
  DISTINCT author_lname
FROM books;
--
  -- unique values, error: two different 'harris' now combined
SELECT
  DISTINCT CONCAT(author_fname, ' ', author_lname)
FROM books;
-- unique full-name
SELECT
  DISTINCT author_fname,
  author_lname
FROM books;
-- unique full-name for both names
  --
  --
  -- ordering
SELECT
  author_fname,
  author_lname
FROM books
ORDER BY
  author_lname DESC;
--
SELECT
  author_fname,
  author_lname
FROM books
ORDER BY
  2,
  1 ASC;
-- 1 == lname, then fname
  --
  --
  -- limits
SELECT
  released_year,
  title
FROM books
ORDER BY
  released_year DESC
LIMIT
  2, 10;
-- most 2 - 10 recent books
  --
  --
  -- likes
SELECT
  author_fname,
  title
FROM books
WHERE
  author_fname LIKE '%da%';
-- % is wildcard for zero til many, _ is one character