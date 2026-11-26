-- PRODUCTIONS

CREATE TABLE Film (
    film_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    release_date DATE,
    summary TEXT
);

CREATE TABLE Serie (
    serie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary TEXT,
    title VARCHAR(100)
);

CREATE TABLE Season (
    season_number INTEGER NOT NULL,
    serie_id INTEGER NOT NULL,
    summary TEXT,
    PRIMARY KEY (serie_id, season_number),
    FOREIGN KEY (serie_id) REFERENCES Serie(serie_id)
);

CREATE TABLE Episode (
    serie_id INTEGER NOT NULL,
    season_number INTEGER NOT NULL,
    episode_number INTEGER NOT NULL,
    title VARCHAR(100),
    release_date DATE,
    summary TEXT,
    PRIMARY KEY (serie_id,  season_number, episode_number),
    FOREIGN KEY (serie_id,  season_number) REFERENCES Season(serie_id,  season_number)
);

CREATE TABLE Special_presentation (
    special_presentation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    release_date DATE,
    summary TEXT
);

CREATE TABLE One_shot (
    one_shot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    release_date DATE,
    summary TEXT
);

-- Include Web-Series ?

-- UNIVERS

CREATE TABLE Univers (
    univers_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100)
);

CREATE TABLE Film_Univers (
    film_id INTEGER NOT NULL,
    univers_id INTEGER NOT NULL,
    PRIMARY KEY (film_id, univers_id),
    FOREIGN KEY (film_id) REFERENCES Film(film_id),
    FOREIGN KEY (univers_id) REFERENCES Univers(univers_id)
);

CREATE TABLE Episode_Univers (
    serie_id INTEGER NOT NULL,
    season_number INTEGER NOT NULL,
    episode_number INTEGER NOT NULL,
    univers_id INTEGER NOT NULL,
    PRIMARY KEY (serie_id, season_number, episode_number, univers_id),
    FOREIGN KEY (serie_id, season_number, episode_number) REFERENCES Episode(serie_id, season_number, episode_number),
    FOREIGN KEY (univers_id) REFERENCES Univers(univers_id)
);

CREATE TABLE Special_presentation_Univers (
    special_presentation_id INTEGER NOT NULL,
    univers_id INTEGER NOT NULL,
    PRIMARY KEY (special_presentation_id, univers_id),
    FOREIGN KEY (special_presentation_id) REFERENCES Special_presentation(special_presentation_id),
    FOREIGN KEY (univers_id) REFERENCES Univers(univers_id)
);

CREATE TABLE One_shot_Univers (
    one_shot_id INTEGER NOT NULL,
    univers_id INTEGER NOT NULL,
    PRIMARY KEY (one_shot_id, univers_id),
    FOREIGN KEY (one_shot_id) REFERENCES One_shot(one_shot_id),
    FOREIGN KEY (univers_id) REFERENCES Univers(univers_id)
);

-- WATCHED-LIST

CREATE TABLE User (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100)
);

CREATE TABLE Watched_film (
    user_id INTEGER NOT NULL,
    film_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, film_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (film_id) REFERENCES Film(film_id)
);

CREATE TABLE Watched_episode (
    user_id INTEGER NOT NULL,
    serie_id INTEGER NOT NULL,
    season_number INTEGER NOT NULL,
    episode_number INTEGER NOT NULL,
    PRIMARY KEY (user_id, serie_id, season_number, episode_number),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (serie_id, season_number, episode_number) REFERENCES Episode(serie_id, season_number, episode_number)
);

CREATE TABLE Watched_special_presentation (
    user_id INTEGER NOT NULL,
    special_presentation_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, special_presentation_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (special_presentation_id) REFERENCES Special_presentation(special_presentation_id)
);

CREATE TABLE Watched_one_shot (
    user_id INTEGER NOT NULL,
    one_shot_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, one_shot_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (one_shot_id) REFERENCES One_shot(one_shot_id)
);