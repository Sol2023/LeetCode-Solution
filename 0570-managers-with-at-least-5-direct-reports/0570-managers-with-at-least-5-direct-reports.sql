# Write your MySQL query statement below


select name
from employee e
where e.id in
(select managerId
from employee e
group by managerId
having count(*) >=5) 