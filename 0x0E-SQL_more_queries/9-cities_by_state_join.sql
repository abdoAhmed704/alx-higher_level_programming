--
SELECT id, cities.name, states.name
FROM cities c inner join states s
on s.id = c.state_id;
