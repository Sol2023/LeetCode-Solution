# Write your MySQL query statement below

select T.Department,T.Employee, T.salary as Salary
from 
(select e.name as Employee,
 d.name as Department,
 e.salary,
rank() over (partition by departmentId order by salary desc) as rank_
from employee e 
inner join department d on d.id = e.departmentId
) as T
where T.rank_ =1
