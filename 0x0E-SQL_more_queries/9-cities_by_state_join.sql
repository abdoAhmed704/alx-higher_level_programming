-- LEFT JOIN
SELECT cities.id, cities.name, states.name
FROM cities c left join states s
on s.id = c.state_id;
