-- inner join
SELECT id, name 
FROM cities
WHERE state_id = (SELECT state_id FROM states WHERE name = 'California')
order by cities.id ASC;
