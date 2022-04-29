CREATE TABLE `artists` (
  `artist_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) not NULL,
  PRIMARY KEY (`artist_id`)
);

  
CREATE TABLE `albums` (
  `album_id` int NOT NULL AUTO_INCREMENT,
  `artist_id` int NOT NULL,
  `name` varchar(50) not NULL,
  `release_date` date not NULL,
  PRIMARY KEY (`album_id`,`artist_id`),
  foreign key(`artist_id`) references artists(`artist_id`)
);

CREATE TABLE `songs` (
  `song_id` int NOT NULL AUTO_INCREMENT,
  `album_id` int NULL,
  `artist_id` int NOT NULL,
  `title` varchar(100) not NULL,
  `release_date` date NULL,
  PRIMARY KEY (`song_id`),
  foreign key(`artist_id`) references artists(`artist_id`),
  foreign key(`album_id`) references albums(`album_id`)
);
  
CREATE TABLE `genres` (
  `genre` char(20) not NULL,
  `song_id` int NOT NULL,
  foreign key(`song_id`) references songs(`song_id`)
);

CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
   PRIMARY KEY(`user_id`)
);

CREATE TABLE `playlist_control` (
  `playlist_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `title` varchar(50) NOT NULL,
  `date_time` datetime NOT NULL,
   PRIMARY KEY(`playlist_id`),
   foreign key(`user_id`) references users(`user_id`),
   unique(`title`,`user_id`),
   unique(`date_time`,`user_id`)
);

CREATE TABLE `playlists`(
  `playlist_id` int NOT NULL,
  `song_id` int NOT NULL, 
   PRIMARY KEY(`playlist_id`,`song_id`)
);

CREATE TABLE `ratings` (
  `rating_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `album_id` int NULL,
  `playlist_id` int NULL,
  `song_id` int NULL,  
  `rating_date` int NULL,
  PRIMARY KEY (`rating_id`),
  `album_rating` tinyint NULL check (album_rating >0 and album_rating <=5),
  `playlist_rating` tinyint NULL check (playlist_rating >0 and playlist_rating <=5),
  `song_rating` tinyint NULL check (song_rating >0 and song_rating <=5),
  foreign key(`user_id`) references users(`user_id`),
  foreign key(`album_id`) references albums(`album_id`),
  foreign key(`song_id`) references songs(`song_id`)
);