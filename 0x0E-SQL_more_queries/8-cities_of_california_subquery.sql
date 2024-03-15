-- inner join
SELECT id, name
FROM cities
WHERE cities.state_id = states.id
WHERE states.name = 'California'
order by cities.id ASC;

