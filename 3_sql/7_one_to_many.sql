DROP DATABASE sql_course;
CREATE DATABASE sql_course;
USE sql_course;
--
-- Create
CREATE TABLE customers(
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  email VARCHAR(100)
);
--
CREATE TABLE orders(
  id INT AUTO_INCREMENT PRIMARY KEY,
  order_date DATE,
  amount DECIMAL(8, 2),
  customer_id INT,
  FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE CASCADE --
  -- ON DELETE CASCADE will delete related orders when customer is deleted
);
--
-- Inserting
INSERT INTO customers (first_name, last_name, email)
VALUES
  ('Boy', 'George', 'george@gmail.com'),
  ('George', 'Michael', 'gm@gmail.com'),
  ('David', 'Bowie', 'david@gmail.com'),
  ('Blue', 'Steele', 'blue@gmail.com'),
  ('Bette', 'Davis', 'bette@aol.com');
--
INSERT INTO orders (order_date, amount, customer_id)
VALUES
  ('2016/02/10', 99.99, 1),
  ('2017/11/11', 35.50, 1),
  ('2014/12/12', 800.67, 2),
  ('2015/01/03', 12.50, 2),
  ('1999/04/11', 450.25, 5);
--
  -- Querying
SELECT
  *
FROM customers
WHERE
  id = 1;
--
SELECT
  *
FROM orders
WHERE
  customer_id = 1;
-- Combining with sub-query
SELECT
  *
FROM orders
WHERE
  customer_id = (
    SELECT
      id
    FROM customers
    WHERE
      id = 1
  );
--
  -- useless, takes all combinations,
  -- cross-join / implicit join
SELECT
  *
FROM customers,
  orders;
--
  -- Implicit inner JOIN with WHERE
SELECT
  email,
  amount
FROM customers,
  orders
WHERE
  customers.id = orders.customer_id;
--
  -- better, EXPLICIT with JOIN
SELECT
  first_name,
  last_name,
  email,
  amount
FROM customers
JOIN orders ON customers.id = orders.customer_id;
--
SELECT
  first_name,
  last_name,
  SUM(amount) AS total_spent
FROM customers
JOIN orders ON customers.id = orders.customer_id
GROUP BY
  orders.customer_id
ORDER BY
  total_spent DESC;
--
  -- Left JOIN
SELECT
  last_name,
  email,
  IFNULL(SUM(amount), 0) AS total_spent
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
GROUP BY
  customers.id
ORDER BY
  total_spent;
--
  -- Right JOIN
SELECT
  last_name,
  email,
  IFNULL(SUM(amount), 0) AS total_spent
FROM customers
RIGHT JOIN orders ON customers.id = orders.customer_id
GROUP BY
  customers.id
ORDER BY
  total_spent;
--
  -- DELETE and CASCADE (see table definition)
DELETE FROM customers
WHERE
  id = 1;
--
SELECT
  customers.id,
  first_name,
  last_name,
  email,
  amount
FROM customers
JOIN orders ON customers.id = orders.customer_id;
--