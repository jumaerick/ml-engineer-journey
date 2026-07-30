create a query that lists suppliers with products priced under 20.

SELECT SupplierName FROM suppliers WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20)

-- ANY operator
SELECT ProductName FROM Products
WHERE ProductID = ANY (
  SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10
);

-- ALL Ooperator
Returns TRUE if all subquery values meet the condition

SELECT ProductName
FROM Products
WHERE ProductID = ALL
(SELECT ProductID FROM OrderDetails);

-- SELECT INTO
used to create a new table and fill values from an existing table

SELECT * INTO CustomersBackup2026
FROM Customers;

SELECT column1, column2 INTO newtable FROM oldtable

-- CREATE a new empty table

SELECT INTO newtable FROM oldtable WHERE 1=0

-- INSERT INTO SELECT statement

Used to copy data from an existing table and insert it into another existing table.

The INSERT INTO SELECT statement requires that the data types in source and target tables match.

INSERT INTO target_table
SELECT * FROM source_table
WHERE condition;

INSERT INTO target_table (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM source_table
WHERE condition;

Copy only the German suppliers into "Customers":

INSERT INTO Customers 
SELECT * FROM suppliers WHERE country ='Germany'