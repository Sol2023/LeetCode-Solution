# Write your MySQL query statement below

select 
d.id,
sum(case when d.month = 'Jan' then revenue else null end) as Jan_Revenue,
sum(case when d.month = 'Feb' then revenue else null end) as Feb_Revenue,
sum(case when d.month = 'Mar' then revenue else null end) as Mar_Revenue,
sum(case when d.month = 'Apr' then revenue else null end) as Apr_Revenue,
sum(case when d.month = 'May' then revenue else null end) as May_Revenue,
sum(case when d.month = 'Jun' then revenue else null end) as Jun_Revenue,
sum(case when d.month = 'Jul' then revenue else null end) as Jul_Revenue,
sum(case when d.month = 'Aug' then revenue else null end) as Aug_Revenue,
sum(case when d.month = 'Sep' then revenue else null end) as Sep_Revenue,
sum(case when d.month = 'Oct' then revenue else null end) as Oct_Revenue,
sum(case when d.month = 'Nov' then revenue else null end) as Nov_Revenue,
sum(case when d.month = 'Dec' then revenue else null end) as Dec_Revenue

from
    Department as d
group by d.id
order by d.id
