-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT tv_genres.name As 'genre', count(tv_show_genres.genre_id) AS 'number_of_shows' 
FROM tv_genres JOIN tv_show_genres
on tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
