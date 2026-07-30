A stored procedure is a precompiled SQL code that can be saved and reused.

Code Reusability - The same procedure can be called from various applications
Improved Performance - Stored procedures are precompiled and runs faster
Database Security - You can set users permission to run a specific procedure (limits direct access to tables)
Easy Maintenance - When updating a procedure, it automatically updates all its use

-- MICROSOFT SQL
CREATE PROCEDURE procedure_name
  @param1 datatype,
  @param2 datatype
AS
BEGIN
  -- SQL_statements to be executed
  SELECT column1, column2
  FROM table_name
  WHERE columnN = @paramN;
END;

EXEC procedure_name @param1 = 'value1', @param2 = 'value2';

DROP PROCEDURE procedure_name;

-- MySQL

DELIMITER //

CREATE PROCEDURE GetTempHumData(IN City VARCHAR(50))
BEGIN
    SELECT * FROM temp_hum_data WHERE sid = City;
END //

DELIMITER ;

CALL GetTempHumData('s1')

Comments/
To explain sections of SQL code or prevent execution

-- Single line comment
/*
Multiple line comment
*/