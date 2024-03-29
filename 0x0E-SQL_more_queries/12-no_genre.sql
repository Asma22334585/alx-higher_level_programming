-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT shows.title AS title, genres.genre_id AS genre_id
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS genres ON shows.id = genres.show_id
WHERE genre_id IS NULL
ORDER BY title ASC, genre_id ASC;
