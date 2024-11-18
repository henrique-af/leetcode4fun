CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    SELECT salary INTO result
    FROM (SELECT DISTINCT salary, RANK() OVER(ORDER BY Salary DESC) r 
          FROM Employee
          GROUP BY salary) T
    WHERE r=N;
    RETURN result;
END;