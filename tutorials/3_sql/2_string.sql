source 2_data.sql --
-- string manipulation
SELECT
  CONCAT('HELLO', ' ... ', 'WORLD')
FROM books;
--
  -- concatenating
  --
SELECT
  author_fname AS First,
  author_lname AS Last,
  CONCAT(author_fname, ' ', author_lname) AS Full
FROM books;
-- separator between all items
SELECT
  author_fname AS First,
  author_lname AS Last,
  CONCAT_WS(' - ', author_fname, author_lname) AS Full
FROM books;
--
  -- parts of string
  --
SELECT
  SUBSTRING('Hello World!', 1, 4);
-- 1-indexed
SELECT
  SUBSTR('Hello World!', 4);
-- until end
SELECT
  SUBSTRING('Hello World!', -4);
-- from end
SELECT
  CONCAT(SUBSTRING('Hello World!', 1, 5), '...');
--
  -- replace
  --
SELECT
  REPLACE('Hello World!', 'o', 'O');
-- case sensitive
SELECT
  REPLACE(title, 'e', '3')
FROM books;
--
  -- reverse
  --
SELECT
  REVERSE('Hello World!');
--
  -- character length
  --
SELECT
  CHAR_LENGTH('Hello World!');
SELECT
  CHAR_LENGTH(author_lname)
FROM books;
--
  -- Upper / Lower
  --
SELECT
  LOWER(author_fname),
  UPPER(author_lname)
FROM books;