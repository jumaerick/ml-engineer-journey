# Which SQL statement is used to select all records from a table named 'Customers'?

SELECT * FROM customers;

# What is a table in a database?
A structured set of data organized in rows and columns

Are SQL keywords case-sensitive?

-- Yes, they are case-sensitive.
No

-- Why is a semicolon used at the end of SQL statements?
To separate multiple SQL statements

-- What is the purpose of the SQL SELECT statement?
To select data from a database

-- How would you select the 'CustomerName' and 'City' columns from a table named 'Customers'?

-- Which of the following SQL statements would return a list of all unique countries from a table named 'Customers'?
SELECT DISTINCT countries FROM Customers;

-- Select count distinct count countries
SELECT COUNT(DISTINCT Country) FROM Customers;

-- What is the purpose of the SQL WHERE clause?
To filter records that meet a specified condition

-- Which of the following SQL statements would return all customers from 'Mexico'?
SELECT * FROM Customers WHERE Country='Mexico'

-- Drag and drop to select all customers with a CustomerID greater than 50.
SELECT * FROM Customers where id > 50;

-- What is the purpose of the SQL ORDER BY keyword?
sorts the results based on specifc=ic column

-- Which SQL statement sorts products from highest to lowest price?
SELECT * FROM Products ORDER BY Price DESC;

-- Select all records from the Customers table, sort the result alphabetically, first by the column Country, then, by the column City.
SELECT * FROM Customers ORDER BY Country, City

-- The AND operator is used to filter records based on more than one condition.

-- All customers from Spain whose names start with 'G'
SELECT * FROM Customers
WHERE Country = 'Spain'
AND CustomerName LIKE 'G%';

-- Customers from Germany in Berlin with a PostalCode over 12000
SELECT * FROM Customers
WHERE Country = 'Germany'
AND City = 'Berlin' AND PostalCode > 12000;

-- Select all records where the City column has the value 'Berlin' and the PostalCode column has the value 12209.
SELECT * FROM Customers where City='Berlin' and PostalCode=12209

-- The OR operator filter records based on multiple conditions where at least one condition is true

-- Select all records where the City column has the value 'Berlin' OR 'London'.
SELECT * FROM Customers where City='Berlin' OR City=='London';

-- Which SQL query would select all customers from either Germany or Spain?
SELECT * FROM Customers WHERE Country='Germany' OR Country='Spain'

-- Which SQL query would select all Spanish customers whose names start with 'G' or 'R'?
SELECT * FROM Customers where Country='Spain' AND (CustomerName LIKE '%G' OR CustomerName LIKE '%R');

-- Logical NOT is used to Negate a specifi condition(s)
-- To filter records that do not match a specified condition
SELECT * FROM Customers WHERE NOT City = 'Berlin';

-- Select the correct statements to return all customers whose names do NOT start with the letter 'A':
SELECT * FROM Customers WHERE NOT CustomerName LIKE '%A'

-- Which SQL statement would select all customers whose CustomerID is NOT between 10 and 50?
SELECT * FROM Customers WHERE CustomerID NOT BETWEEN (10, 50)

-- Which query will select customers who are NOT located in 'Paris' or 'London'?
SELECT * FROM Customers WHERE City NOT IN ('Paris', 'London');

-- INSERT for adding new records into a table
Drag and drop the correct syntax to insert data into the Customers table for specified columns:
INSERT INTO Customers (CustomerName, Country, City) VALUES ('Erick', 'Kenya', 'Nairobi')

-- How can you insert multiple rows with a single INSERT INTO statement in SQL?
INSERT INTO Customers (CustomerName, Country, City) VALUES ('Erick', 'Kenya', 'Nairobi'),  ('Jimmy', 'Uganda', 'Kampala')

-- NULL is a field with no value

-- What is the purpose of the SQL UPDATE statement?
To modify existing records in a table

Update the City column of all records in the Customers table.
UPDATE Customers SET City='Oslo';

Update the City value and the Country value.

UPDATE Customers SET City='Oslo', Country='Norway' WHERE CustomerID = 32;

-- DELETE remove existing records from the table
-- Delete all the records from the Customers table where the Country value is 'Norway'.
DELETE FROM Customers WHERE cOUNTRY='Norway';

SELECT TOP 5 * FROM Customers;
SELECT the first five
SELECT * FROM Customers LIMIT 5;

-- MIN MAX
-- Min returns smallest value of the selected column
Use the MIN function to select the record with the smallest value of the Price column.
SELECT MIN(Price) FROM Customers;

-- COUNT returns the number of rows that match a specifi cretirion
function to return the number of records that have the Price value set to 18.
SELECT COUNT(*) FROM Customers WHERE Price=18;

-- Which keyword can be used to ignore duplicates?

-- SUM returns total sum of a numerical column

Use an SQL function to calculate the sum of all the Price column values in the Products table.

SELECT SUM(Price) FROM Products;

-- AVG calculates the average of a numeric column
Query to return the average price of products?
SELECT AVG(price) FROM Products;
Ignores NULL Values

-- LIKE Operator records that match specific pattern
Return all customers with names starting with 'H'?
_ Represents any single charater

Select all records where the value of the City column starts with the letter "a".
SELECT * FROM Customers WHERE City LIKE 'a%'
Ends with
SELECT * FROM Customers WHERE City LIKE '%a'
Contains
SELECT * FROM Customers WHERE City LIKE '%a%'

Select all records where the value of the City column starts with letter "a" and ends with the letter "b".
SELECT * FROM Customers WHERE City LIKE 'a%b'

NOT start with the letter "a".
SELECT * FROM Customers WHERE City NOT LIKE 'a%'