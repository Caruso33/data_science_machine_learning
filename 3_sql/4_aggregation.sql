source 3_data.sql;
--
--
-- count
SELECT
  COUNT(*)
FROM books;
--
SELECT
  COUNT(DISTINCT author_fname, author_lname) AS Uniq_Authors
FROM books;
--
SELECT
  COUNT(title) AS Titles
FROM books
WHERE
  title LIKE '%the%';
--
  --
  -- grouping
SELECT
  author_fname,
  author_lname,
  COUNT(*)
FROM books
GROUP BY
  author_lname,
  author_fname;
--
SELECT
  CONCAT(
    'In ',
    released_year,
    ' ',
    COUNT(*),
    ' book(s) released'
  ) AS Year
FROM books
GROUP BY
  released_year;
--
  --
  -- min / maxSELECT
SELECT
  MIN(released_year)
FROM books;
--
  -- SELECT
  --   MAX(pages),
  --   title
  -- FROM books;
  -- does not work, titles are independent
  -- sub-query to the help
SELECT
  pages,
  title
FROM books
WHERE
  pages =(
    SELECT
      Max(pages)
    FROM books
  );
-- or ORDER BY
SELECT
  pages,
  title
FROM books
ORDER BY
  pages ASC
LIMIT
  1;
--
  --
  -- min + group > find min(year) of each author
SELECT
  author_fname,
  author_lname,
  Min(released_year)
FROM books
GROUP BY
  author_lname,
  author_fname;
--
  --
  -- sum
SELECT
  Sum(pages)
FROM books;
--
  --
  -- avg
SELECT
  Avg(pages)
FROM books;