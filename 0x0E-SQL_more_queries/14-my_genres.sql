-- a script that uses the hbtn_0d_tvshows database to
-- lists all genres of the show Dexter
SELECT tvg.name
FROM tv_genres AS tvg
     JOIN tv_show_genres AS tvsg
     	  ON tvg.id = tvsg.genre_id
     JOIN tv_shows AS tvs
     	  ON tvsg.show_id = tvs.id
WHERE tvs.title = "Dexter"
ORDER BY tvg.name;
