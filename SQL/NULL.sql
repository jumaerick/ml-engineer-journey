Represents missing data or unknown value

COALESCE() - The preferred standard. (Works in MySQL, SQL Server and Oracle)
IFNULL() - (MySQL)
ISNULL() - (SQL Server)
NVL() - (Oracle)
IsNull() - (MS Access)

-- COALESCE replaces nulls with zero
SELECT ProductName, Price * (InStock + COALESCE(InOrder, 0))
FROM Products;

IFNULL() function replaces NULL with a specified value.
IFNULL(expr, alt)

SELECT ProductName, Price * (InStock + IFNULL(InOrder, 0))
FROM Products;

ISNULL(expr, alt)

SELECT ProductName, Price * (InStock + ISNULL(InOrder, 0))
FROM Products;