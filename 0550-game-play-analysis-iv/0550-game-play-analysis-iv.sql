# Write your MySQL query statement below
WITH FirstDay AS(
    SELECT player_id, MIN(event_date) as first_date
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(
        COUNT(a.player_id) / 
        (SELECT COUNT(DISTINCT(b.player_id)) 
        FROM Activity b), 
    2) AS fraction
FROM Activity a
LEFT JOIN FirstDay f on a.player_id = f.player_id
WHERE DATEDIFF(a.event_date, f.first_date) = 1;