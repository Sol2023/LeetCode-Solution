# Write your MySQL query statement below

# SELECT S.score, COUNT(S2.score) as `rank`
# FROM Scores S,
# (SELECT DISTINCT score FROM Scores) S2
# WHERE S.score<=S2.score
# GROUP BY S.id
# ORDER BY S.score DESC;

select s.score, dense_rank() over(order by s.score desc) `rank`
from Scores s