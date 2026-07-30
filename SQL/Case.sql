The CASE expression is used to define different results based on specified conditions in an SQL statement.

CASE
  WHEN condition1 THEN result1
  WHEN condition2 THEN result2
  WHEN conditionN THEN resultN
  ELSE default_result
END;


SELECT ProductName, Price,
CASE
  WHEN Price < 20 THEN 'Low Cost'
  WHEN Price BETWEEN 20 AND 50 THEN 'Medium Cost'
  ELSE 'High Cost'
END AS PriceCategory
FROM Products;

If there is no ELSE clause and no conditions are true, it returns NULL.