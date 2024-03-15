--
SELECT tv_genres.name
FROM tv_genres 
JOIN tv_show_genres on tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows on tv_show_genres.show_id = tv_shows.id
where tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY tv_genres.name ASC;
