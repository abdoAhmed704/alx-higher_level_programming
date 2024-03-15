-- inner join
SELECT id, name 
FROM cities
WHERE cities.state_id = states.state_id
order by cities.id ASC;
