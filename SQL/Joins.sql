SELECT 5 + 10 as sum;

-- Inner join returns all of the records in table_a that have matching records in table_b

SELECT * FROM users us
JOIN orders od
ON us.id = od.user_id;

-- LEFT JOIN  return every record from table_a regardless of whether or not any of those records have a match in table_b
SELECT * FROM users us
LEFT JOIN orders od
ON us.id = od.user_id;

-- LEFT JOIN return all records from table_b regardless of matches, and all matching records between the two tables.
SELECT * FROM users us
RIGHT JOIN orders od
ON us.id = od.user_id;

-- FULL JOIN
It returns all records from both from table_a and table_b regardless of whether or not they have matches

Select all records where the second letter of the City is an "a".
SELECT * FROM records where name LIKE '_a%';

How do you specify a range of characters in SQL using wildcards?

Select all records where the first letter of the City is an "a" or a "c" or an "s".

SELECT * FROM Customers
WHERE City LIKE '[acs]%';

Select all records where the first letter of the City starts with anything from an "a" to an "f".

SELECT * FROM Customers
WHERE City LIKE '[a-f]%';

Select all records where the first letter of the City is NOT an "a" or a "c" or an "f".
SELECT * FROM Customers
WHERE City LIKE '[!acf]%';

Drag and drop the correct wildcard to select cities that start with 'L' and end with 'n'.
SELECT * FROM Customers WHERE City LIKE 'L%n'

-- Which SQL statement selects all products with a price between 10 and 20?
SELECT * FROM products WHERE price BETWEEN 10 AND 20;

Use the BETWEEN operator to select all the records where the value of the ProductName column is alphabetically between 'Geitost' and 'Pavlova'.
SELECT * FROM Products WHERE ProductName BETWEEN 'Geitost' AND 'Pavlova';

SELECT ProductName AS [Great Products]

What is the purpose of a self join in SQL?

To join a table with itself

SELECT A.CustomerName, B.CustomerName
FROM Customers A, Customers B
WHERE A.City = B.City;

What is the primary purpose of the SQL UNION operator?
To combine the result-sets of two or more SELECT statements

What is the key difference between UNION and UNION ALL?

UNION removes duplicates by default, while UNION ALL includes all rows

Which condition must be met when using the UNION operator?
The SELECT statements must have the same number of columns with similar data types

SELECT City FROM Customers

SELECT City FROM Suppliers
ORDER BY City;

What is the primary purpose of the SQL GROUP BY statement?
To group rows with the same values into summary rows

How can you sort the results of a GROUP BY statement?
Use the ORDER BY clause after the GROUP BY clause

Why can't the WHERE clause be used with aggregate functions?
Aggregate functions are evaluated after the WHERE clause

