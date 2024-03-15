-- inner join
SELECT id, name 
FROM cities
WHERE cities.state_id = states.state_id
WHERE name = 'California'
order by cities.id ASC;
