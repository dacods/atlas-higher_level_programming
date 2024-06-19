-- list all genres from database and display number of shows linked to each
SELECT genres.name AS genre, 
    COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
JOIN genres ON tv_show_genres.genre_id = genres.id
GROUP BY genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;