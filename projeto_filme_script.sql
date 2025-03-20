-- movies definition
CREATE TABLE movies (
	id VARCHAR(50),
	Title VARCHAR(64),
	"Movie Link" VARCHAR(50),
	"Year" INTEGER,
	Duration VARCHAR(50),
	MPA VARCHAR(50),
	Rating REAL,
	Votes VARCHAR(50)
);


-- movies insertion
INSERT INTO movies as m
SELECT
	ID, Title, "Movie Link", Year, Duration, MPA, Rating, Votes
FROM
	movies_ds as mds


--genres definition
CREATE TABLE genres (
	id INTERGER,
	genres VARCHAR (128)
);


--genres insertion
INSERT INTO genres as g
SELECT
	rowid,
	genres
FROM
	movies_ds;


--stars definition
CREATE TABLE stars(
	id INTERGER,
	stars VARCHAR (128)
)


--stars insertion
INSERT INTO stars as s
SELECT
	rowid, 
	stars	
FROM 
	movies_ds;


