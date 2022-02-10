# Write your MySQL query statement below

select agg.email as Email from
(select p.email, count(*) as c from Person p group by p.email having c>=2) agg