# Write your MySQL query statement below


select d.name as Department,
e.name as Employee, 
e.salary
from Employee e
left join Department d on e.departmentId = d.id
where (e.departmentId, e.salary) in (
    select
        DepartmentId, Max(salary)
    from 
        Employee
    group by DepartmentId
)