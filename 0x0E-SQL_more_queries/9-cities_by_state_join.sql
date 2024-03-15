-- LEFT JOIN
SELECT cities.id, cities.name, states.name FROM cities left join states on states.id = cities.state_id ORDER BY cities.id;
