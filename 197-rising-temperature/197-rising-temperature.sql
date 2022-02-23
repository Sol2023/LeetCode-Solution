# Write your MySQL query statement below

# select w2.id
# from 
#     Weather w1,
#     Weather w2
# where 
#     datediff(w1.recordDate, w2.recordDate)=-1 
#     and w1.temperature < w2.temperature

SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.recordDate, w.recordDate) = 1
        AND weather.Temperature > w.Temperature