# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
songs_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id varchar,   
    start_time timestamp NOT NULL,
    user_id int NOT NULL,
    level varchar NOT NULL,
    song_id varchar,
    artist_id varchar,
    session_id int NOT NULL,
    location varchar NOT NULL,
    user_agent varchar  NOT NULL,
    PRIMARY KEY(songplay_id, start_time, user_id)
);
""")

user_table_create = (""" 
CREATE TABLE IF NOT EXISTS users (
user_id int PRIMARY KEY,
first_name varchar(255) ,
last_name varchar(255),
gender varchar(255),
level varchar(255)
);
""")

songs_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
song_id varchar(255) PRIMARY KEY,
song_title varchar (255) NOT NULL,
artist_id varchar (255) NOT NULL,
release_year int,
duration decimal
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
artist_id varchar PRIMARY KEY,
name varchar(255),
location varchar(255),
latitude varchar(255),
longitude varchar(255));
""")
#start_time varchar(255) PRIMARY KEY was start_time timestamp PRIMARY KEY,
time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
start_time timestamp PRIMARY KEY,
hour int,
day int,
week int,
month int,
year int,
weekday int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO UPDATE
SET level = EXCLUDED.level;
""")

songs_table_insert = ("""
INSERT INTO songs (song_id, song_title, artist_id, release_year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id)
DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id)
DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time)
DO NOTHING
""")

# FIND SONGS
#WHERE song_title = %s was WHERE song = %s
song_select = (""" 
SELECT songs.song_id, songs.artist_id FROM songs
JOIN artists ON artists.artist_id = songs.artist_id
WHERE song_title = %s

AND name = %s
AND duration = %s;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, songs_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, songs_table_drop, artist_table_drop, time_table_drop]