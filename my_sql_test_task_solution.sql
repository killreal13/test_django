USE test_schema;


SELECT bid.client_number AS client_number, COUNT(CASE event_value.outcome WHEN 'win' THEN 1 ELSE NULL END) AS Побед, COUNT(CASE event_value.outcome WHEN 'lose' THEN 1 ELSE NULL END) AS Поражений
FROM bid
LEFT JOIN event_value
ON bid.play_id = event_value.play_id
GROUP BY client_number
ORDER BY client_number;


SELECT CONCAT(home_team, "-", away_team) AS game, COUNT(*) AS games_count
FROM event_entity
GROUP BY home_team
ORDER BY games_count;