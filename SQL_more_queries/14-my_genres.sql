-- List all genres of a show from a database
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN tv_genres ON tv_show_genres.tv_genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;