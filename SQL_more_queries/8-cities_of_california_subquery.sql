-- List all of the cities of California that can be found in the database
SELECT @california_id := id FROM states WHERE name = 'California';

SELECT id, name FROM cities WHERE state_id = @california_id ORDER BY id ASC;