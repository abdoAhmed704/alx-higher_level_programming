-- LEFT JOIN
-- AHA
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states on states.id = cities.state_id ORDER BY cities.id;
