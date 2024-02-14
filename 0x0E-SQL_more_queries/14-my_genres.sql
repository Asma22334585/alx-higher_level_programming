-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT genres.name AS name
FROM tv_shows AS shows
INNER JOIN tv_show_genres AS show_genres ON shows.id = show_genres.show_id
INNER JOIN tv_genres AS genres ON genres.id = show_genres.genre_id
WHERE shows.title = "Dexter"
ORDER BY name ASC;
