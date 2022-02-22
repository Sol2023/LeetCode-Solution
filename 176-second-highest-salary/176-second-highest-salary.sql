# Write your MySQL query statement below

SELECT IFNULL((SELECT DISTINCT e.salary 
               FROM Employee AS e 
               ORDER BY e.salary DESC LIMIT 1 OFFSET 1), 
              NULL)
AS SecondHighestSalary