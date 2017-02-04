BEGIN TRANSACTION;
CREATE TABLE movies (
	movie_id INTEGER NOT NULL, 
	title VARCHAR(64), 
	released_at TIMESTAMP, 
	imdb_url VARCHAR(200), 
	PRIMARY KEY (movie_id)
);
INSERT INTO "movies" VALUES(1,'Toy Story','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)');
INSERT INTO "movies" VALUES(2,'GoldenEye','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?GoldenEye%20(1995)');
INSERT INTO "movies" VALUES(3,'Four Rooms','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Four%20Rooms%20(1995)');
INSERT INTO "movies" VALUES(4,'Get Shorty','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Get%20Shorty%20(1995)');
INSERT INTO "movies" VALUES(5,'Copycat','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Copycat%20(1995)');
INSERT INTO "movies" VALUES(6,'Shanghai Triad (Yao a yao yao dao waipo qiao)','1995-01-01 00:00:00.000000','http://us.imdb.com/Title?Yao+a+yao+yao+dao+waipo+qiao+(1995)');
INSERT INTO "movies" VALUES(7,'Twelve Monkeys','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Twelve%20Monkeys%20(1995)');
INSERT INTO "movies" VALUES(8,'Babe','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Babe%20(1995)');
INSERT INTO "movies" VALUES(9,'Dead Man Walking','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Dead%20Man%20Walking%20(1995)');
INSERT INTO "movies" VALUES(10,'Richard III','1996-01-22 00:00:00.000000','http://us.imdb.com/M/title-exact?Richard%20III%20(1995)');
INSERT INTO "movies" VALUES(11,'Seven (Se7en)','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Se7en%20(1995)');
INSERT INTO "movies" VALUES(12,'Usual Suspects, The','1995-08-14 00:00:00.000000','http://us.imdb.com/M/title-exact?Usual%20Suspects,%20The%20(1995)');
INSERT INTO "movies" VALUES(13,'Mighty Aphrodite','1995-10-30 00:00:00.000000','http://us.imdb.com/M/title-exact?Mighty%20Aphrodite%20(1995)');
INSERT INTO "movies" VALUES(14,'Postino, Il','1994-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Postino,%20Il%20(1994)');
INSERT INTO "movies" VALUES(15,'Mr. Holland''s Opus','1996-01-29 00:00:00.000000','http://us.imdb.com/M/title-exact?Mr.%20Holland''s%20Opus%20(1995)');
INSERT INTO "movies" VALUES(16,'French Twist (Gazon maudit)','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Gazon%20maudit%20(1995)');
INSERT INTO "movies" VALUES(17,'From Dusk Till Dawn','1996-02-05 00:00:00.000000','http://us.imdb.com/M/title-exact?From%20Dusk%20Till%20Dawn%20(1996)');
INSERT INTO "movies" VALUES(18,'White Balloon, The','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Badkonake%20Sefid%20(1995)');
INSERT INTO "movies" VALUES(19,'Antonia''s Line','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Antonia%20(1995)');
INSERT INTO "movies" VALUES(20,'Angels and Insects','1995-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Angels%20and%20Insects%20(1995)');
INSERT INTO "movies" VALUES(21,'Muppet Treasure Island','1996-02-16 00:00:00.000000','http://us.imdb.com/M/title-exact?Muppet%20Treasure%20Island%20(1996)');
INSERT INTO "movies" VALUES(22,'Cape Fear','1991-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Cape%20Fear%20(1991)');
INSERT INTO "movies" VALUES(23,'Cape Fear','1962-01-01 00:00:00.000000','http://us.imdb.com/M/title-exact?Cape%20Fear%20(1962)');
CREATE TABLE users (
	user_id INTEGER NOT NULL, 
	email VARCHAR(64), 
	password VARCHAR(64), 
	age INTEGER, 
	zipcode VARCHAR(15), 
	PRIMARY KEY (user_id)
);
INSERT INTO "users" VALUES(1,NULL,NULL,24,'85711');
INSERT INTO "users" VALUES(2,NULL,NULL,53,'94043');
INSERT INTO "users" VALUES(3,NULL,NULL,23,'32067');
INSERT INTO "users" VALUES(4,NULL,NULL,24,'43537');
INSERT INTO "users" VALUES(5,NULL,NULL,33,'15213');
INSERT INTO "users" VALUES(6,NULL,NULL,42,'98101');
INSERT INTO "users" VALUES(7,'cats@gmail.com',NULL,57,'91344');
INSERT INTO "users" VALUES(8,NULL,NULL,36,'05201');
INSERT INTO "users" VALUES(9,NULL,NULL,29,'01002');
INSERT INTO "users" VALUES(10,NULL,NULL,53,'90703');
INSERT INTO "users" VALUES(11,NULL,NULL,39,'30329');
INSERT INTO "users" VALUES(12,NULL,NULL,28,'06405');
INSERT INTO "users" VALUES(13,NULL,NULL,47,'29206');
INSERT INTO "users" VALUES(14,NULL,NULL,45,'55106');
INSERT INTO "users" VALUES(15,NULL,NULL,49,'97301');
INSERT INTO "users" VALUES(16,NULL,NULL,21,'10309');
INSERT INTO "users" VALUES(17,NULL,NULL,30,'06355');
INSERT INTO "users" VALUES(18,NULL,NULL,35,'37212');
INSERT INTO "users" VALUES(19,NULL,NULL,40,'02138');
INSERT INTO "users" VALUES(20,NULL,NULL,42,'95660');
INSERT INTO "users" VALUES(21,NULL,NULL,26,'30068');
CREATE TABLE ratings (
	rating_id INTEGER NOT NULL, 
	movie_id INTEGER, 
	user_id INTEGER, 
	score INTEGER, 
	PRIMARY KEY (rating_id), 
	FOREIGN KEY(movie_id) REFERENCES movies (movie_id), 
	FOREIGN KEY(user_id) REFERENCES users (user_id)
);
INSERT INTO "ratings" VALUES(1,20,1,3);
INSERT INTO "ratings" VALUES(2,19,2,3);
INSERT INTO "ratings" VALUES(3,18,4,1);
INSERT INTO "ratings" VALUES(4,17,3,2);
INSERT INTO "ratings" VALUES(5,16,5,1);
INSERT INTO "ratings" VALUES(6,15,6,4);
INSERT INTO "ratings" VALUES(7,14,7,2);
INSERT INTO "ratings" VALUES(8,13,8,5);
INSERT INTO "ratings" VALUES(9,12,9,3);
INSERT INTO "ratings" VALUES(10,21,6,3);
INSERT INTO "ratings" VALUES(11,11,10,2);
INSERT INTO "ratings" VALUES(12,10,11,5);
INSERT INTO "ratings" VALUES(13,9,20,5);
INSERT INTO "ratings" VALUES(14,8,21,3);
INSERT INTO "ratings" VALUES(15,7,6,3);
INSERT INTO "ratings" VALUES(16,6,13,3);
INSERT INTO "ratings" VALUES(17,5,12,5);
INSERT INTO "ratings" VALUES(18,4,19,2);
INSERT INTO "ratings" VALUES(19,3,14,4);
INSERT INTO "ratings" VALUES(20,2,15,2);
INSERT INTO "ratings" VALUES(21,1,11,4);
COMMIT;
