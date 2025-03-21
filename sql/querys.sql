INSERT-> inserir registro
UPDATE -> alterar registro
DELETE -> apagar registro

SELECT -> onde tudo aconte / consultas

SELECT 
 colunas
FROM
 tabelas
CONDIÇOES

-- Consultar filmes genero drama
SELECT * FROM filmes_imdb fi 
WHERE genres LIKE '%Drama%'

-- Consultar filmes ano 2024
SELECT * FROM filmes_imdb fi 
WHERE "Year" = 2024

-- Consultar filmes com buget maior que 5000000
SELECT * FROM filmes_imdb WHERE budget > 5000000;

-- Consultar filmes com ator vin diesel
SELECT * FROM filmes_imdb 
WHERE stars like "%'vin diesel'%";

-- pesquisar apenas filmes com origem no Canadá: 
select * from filmes_imdb fi
where countries_origin LIKE '%Canada%'
 
-- pesquisar apenas filmes em inglês:
select * from filmes_imdb fi
where Languages like '%English%'

-- Consultar filmes com duração superior a 2 horas
SELECT * FROM filmes_imdb fi
WHERE Duration > 2
 
-- Consultar filmes que tiveram uma nota maior que 6
SELECT * FROM filmes_imdb fi
WHERE Rating > 6

SELECT * FROM filmes_imdb fi 
WHERE year = 2024
AND Duration  = '2h 40m'

-- Consultar filmes produzidos pela Disney
SELECT * FROM filmes_imdb2 fi
WHERE production_companies LIKE '%Walt Disney Pictures%'

-- consultar filmes a partir de 2020
SELECT * FROM filmes_imdb fi 
WHERE year >= 2020

-- consultar filmes a partir entre 2020 e 2024
SELECT * FROM filmes_imdb fi 
WHERE "Year" BETWEEN 2020 AND 2024

-- consultar filmes na lista de anos 2020,2021,2022,2023 e 2024
SELECT * FROM filmes_imdb fi 
WHERE "Year" IN(2020,2021,2022,2023,2024)

SELECT * from filmes_imdb fi
where production_companies like '%Universal Pictures%'
and countries_origin like '%United States%'

SELECT Title,"Year", Languages,Rating 
FROM filmes_imdb fi 
WHERE "Year" IN(2020,2021,2022,2023,2024)
ORDER BY Rating


-- AS
-- ASC

SELECT 
	"Year",
	count(*) quantidade,
	sum(Rating) total_rating,
	avg(Rating) media_rating,
	ROUND(avg(Rating),2) media_formata
FROM filmes_imdb fi 
WHERE "Year" IN(2020,2021,2022,2023,2024)
GROUP BY "Year" 

SELECT 
	"Year",
	count(*) quantidade,
	sum(Rating) total_rating,
	avg(Rating) media_rating,
	ROUND(avg(Rating),2) media_formata
FROM filmes_imdb fi 
WHERE "Year" NOT IN(2020,2021,2022,2023,2024)
GROUP BY "Year" 

SELECT 
	budget,
	grossWorldWide,
	gross_US_Canada,
	(grossWorldWide + gross_US_Canada)  gross,
	ROUND( grossWorldWide / budget,2) as tickt
FROM filmes_imdb fi 

SELECT 
	UPPER(title) maiusculo,
	LOWER(title) minusculo
FROM filmes_imdb fi 

SELECT 
	title,
	REPLACE(title,"'",'') titulo2
FROM filmes_imdb fi 

-- Consultar filmes brasileiros lançados 
-- nos anos que teve Copa do Mundo
SELECT * FROM filmes_imdb fi
WHERE "Year" IN (
	SELECT DISTINCT YEAR 
	FROM filmes_imdb 
	WHERE ((YEAR+2)%4) = 0 -- 	
	)
AND countries_origin LIKE '%Brazil%'


-- SQLIte NÃO FUNCIONA
CREATE TABLE filmes 
SELECT 
	ID,Title, "Movie Link", Year, Duration, MPA, Rating, Votes
FROM filmes_imdb fi 





-- filmes definition
CREATE TABLE filmes (
	id VARCHAR(50),
	Title VARCHAR(64),
	"Movie Link" VARCHAR(50),
	"Year" INTEGER,
	Duration VARCHAR(50),
	MPA VARCHAR(50),
	Rating REAL,
	Votes VARCHAR(50)
);

/*
INSERT INTO filmes 
(lista de colunas, coluna1, coluna2)
VALUES
(lista de dados, valor2, valor2)
*/

INSERT INTO filmes
SELECT 
	ID,UPPER(Title), "Movie Link", Year, Duration, MPA, Rating, Votes
FROM filmes_imdb fi 

-- CUIDADO COM DELETE SEM WHERE
DELETE FROM filmes

-- SQLite não tem TRUNCATE 
-- truncate é mais rápido que deletar tudo
TRUNCATE TABLE filmes

-- filmes_imdb definition

CREATE TABLE stars (
	id INTEGER,
	stars VARCHAR(128)
);

CREATE TABLE genres (
	id INTEGER,
	genres VARCHAR(256)
);



INSERT INTO stars 
SELECT 
rowid ,
stars
FROM filmes_imdb 

INSERT INTO genres 
SELECT 
rowid,
genres
FROM filmes_imdb fi 


SELECT 
	fi.id,
	fi.stars,
	fi.genres,
	g.id,
	s.id
FROM filmes_imdb fi
INNER JOIN genres g ON fi.genres = g.genres 
INNER JOIN stars s ON fi.stars = s.stars 

filmes_genres
filmes_stars

SELECT 
	fi.id,
	fi.stars,
	fi.genres,
	g.id,
	s.id
FROM filmes_imdb fi
INNER JOIN genres g ON fi.genres = g.genres 
INNER JOIN stars s ON fi.stars = s.stars 

CREATE TABLE filmes_genres(	
	idfilmes VARCHAR(50),
	idgeners INTEGER
);

CREATE TABLE filmes_stars(	
	idfilmes VARCHAR(50),
	idstars INTEGER
);

INSERT INTO filmes_genres 
SELECT 
	DISTINCT 
	fi.id,
	g.id
FROM filmes_imdb fi
INNER JOIN genres g ON fi.genres = g.genres 



INSERT INTO filmes_stars 
SELECT 
	DISTINCT 
	fi.id,
	s.id
FROM filmes_imdb fi
INNER JOIN stars s ON fi.stars = s.stars



SELECT 
f.*,
s.*



x.rowid 
-- filmes_imdb definition

CREATE TABLE filmes_imdb (
	id VARCHAR(50),
	Title VARCHAR(64),
	"Movie Link" VARCHAR(50),
	"Year" INTEGER,
	Duration VARCHAR(50),
	MPA VARCHAR(50),
	Rating REAL,
	Votes VARCHAR(50),
	budget REAL,
	grossWorldWide REAL,
	gross_US_Canada REAL,
	opening_weekend_Gross REAL,
	directors VARCHAR(64),
	writers VARCHAR(64),
	stars VARCHAR(128),
	genres VARCHAR(256),
	countries_origin VARCHAR(50),
	filming_locations VARCHAR(128),
	production_companies VARCHAR(128),
	Languages VARCHAR(64),
	wins INTEGER,
	nominations INTEGER,
	oscars INTEGER
);


SELECT 
DISTINCT genres 
FROM filmes_imdb 
WHERE genres IS NOT NULL 
AND genres <> "['Drama', 'Romance']" 


SQL -> 
	pl/sql
	t-sql
	pg-sql
	sql
	

/*
Detalhes básicos do filme: título, ano, duração, classificação MPA, classificação IMDb, votos.
Dados financeiros: Orçamento, bruto global, bruto dos EUA/Canadá, ganhos do fim de semana de abertura.
Créditos: Diretores, roteiristas, estrelas.
Detalhes adicionais: gêneros, países, locais de filmagem, produtoras, idiomas.
Prêmios: Vitórias, indicações, indicações ao Oscar.
*/
