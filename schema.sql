-- PRODUCTIONS

CREATE TABLE Film (
    film_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    release_date DATE,
    summary TEXT
);

CREATE TABLE Serie (
    serie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100)
);

CREATE TABLE Season (
    season_number INTEGER NOT NULL,
    serie_id INTEGER NOT NULL,
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