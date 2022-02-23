# Write your MySQL query statement below

# with new_table as (
#     select
#         c.seat_id,
#         c.free,
#         lead(free,1) over(partition by c.seat_id, order by c.free as next_seat
#     from Cinema as c
# )
    

select
distinct c1.seat_id
from 
Cinema as c1
join Cinema as c2 on abs(c1.seat_id -c2.seat_id)=1 and c1.free=1 and c2.free=1
order by c1.seat_id