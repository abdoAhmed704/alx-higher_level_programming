--
SELECT id, name, name
FROM cities c, states s
WHERE s.id = c.state_id;
