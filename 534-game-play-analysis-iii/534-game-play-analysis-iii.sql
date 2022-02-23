# Write your MySQL query statement below

select 
    a.player_id,
    a.event_date,
    sum(a.games_played) over(partition by a.player_id order by a.event_date) as games_played_so_far
from Activity a
order by a.player_id
