import sqlite3

def dbConnection(dbPath : str) -> tuple[sqlite3.Connection, sqlite3.Cursor] :
    con = sqlite3.connect(dbPath)
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    return (con, cur)

#  Productions

def addFilm(con : sqlite3.Connection, cur : sqlite3.Cursor, title : str, release_date : str, summary : str) -> None :
    cur.execute("INSERT INTO Film VALUES (?, ?, ?, ?)", (None, title, release_date, summary))
    con.commit()

def rmFilm(con : sqlite3.Connection, cur : sqlite3.Cursor, film_id : int) -> None :
    cur.execute("DELETE FROM Film WHERE film_id = ?", (film_id,))
    con.commit()

def addSpecialPresentation(con : sqlite3.Connection, cur : sqlite3.Cursor, title : str, release_date : str, summary : str) -> None :
    cur.execute("INSERT INTO Special_presentation VALUES (?, ?, ?, ?)", (None, title, release_date, summary))
    con.commit()

def rmSpecialPresentation(con : sqlite3.Connection, cur : sqlite3.Cursor, special_presentation_id : int) -> None :
    cur.execute("DELETE FROM Special_presentation WHERE special_presentation_id = ?", (special_presentation_id,))
    con.commit()

def addOneShot(con : sqlite3.Connection, cur : sqlite3.Cursor, title : str, release_date : str, summary : str) -> None :
    cur.execute("INSERT INTO One_shot VALUES (?, ?, ?, ?)", (None, title, release_date, summary))
    con.commit()

def rmOneShot(con : sqlite3.Connection, cur : sqlite3.Cursor, one_shot_id : int) -> None :
    cur.execute("DELETE FROM One_shot WHERE one_shot_id = ?", (one_shot_id,))
    con.commit()

def addEpisode(con : sqlite3.Connection, cur : sqlite3.Cursor, serie_id : int, season_number : int, episode_number : int, title : str, release_date : str, summary : str) -> None :
    cur.execute("INSERT INTO Episode VALUES (?, ?, ?, ?, ?, ?)", (serie_id, season_number, episode_number, title, release_date, summary))
    con.commit()
    
def rmEpisode(con : sqlite3.Connection, cur : sqlite3.Cursor, serie_id : int, season_number : int, episode_number : int) -> None :
    cur.execute("DELETE FROM Episode WHERE serie_id = ? AND season_number = ? AND episode_number = ?", (serie_id, season_number, episode_number))

def addSeason(con : sqlite3.Connection, cur : sqlite3.Cursor, serie_id : int, season_number : int, summary : str) -> None :
    cur.execute("INSERT INTO Season VALUES (?, ?, ?)", (serie_id, season_number, summary))
    con.commit()
    
def rmSeason(con : sqlite3.Connection, cur : sqlite3.Cursor, serie_id : int, season_number : int) -> None :
    cur.execute("DELETE FROM Season WHERE serie_id = ? AND season_number = ?", (serie_id, season_number))
    con.commit()

def addSerie(con : sqlite3.Connection, cur : sqlite3.Cursor, title : str, summary : str) -> None :
    cur.execute("INSERT INTO Serie VALUES (?, ?, ?)", (None, title, summary))
    con.commit()
    
def rmSerie(con : sqlite3.Connection, cur : sqlite3.Cursor, serie_id : int) -> None :
    cur.execute("DELETE FROM Serie WHERE serie_id = ?", (serie_id,))
    con.commit()

# Univers

def addUnivers(con : sqlite3.Connection, cur : sqlite3.Cursor, name : str) :
    cur.execute("INSERT INTO Univers VALUES (? ,?)", (None, name))
    con.commit()
    
def rmUnivers(con : sqlite3.Connection, cur : sqlite3.Cursor, univers_id : int) -> None :
    cur.execute("DELETE FROM Univers WHERE univers_id = ?", (univers_id,))
    con.commit()

def linkFilmUnivers(con : sqlite3.Connection, cur : sqlite3.Cursor, film_id : int, univers_id : int) :
    cur.execute("INSERT INTO Film_Univers VALUES (?, ?)", (film_id, univers_id))
    con.commit()

def UnlinkFilmUnivers(con : sqlite3.Connection, cur : sqlite3.Cursor, film_id : int, univers_id : int) :
    cur.execute("DELETE FROM Film_Univers WHERE film_id = ? and univers_id = ?", (film_id, univers_id))
    con.commit()

def linkEpisodeUnivers(con : sqlite3.Connection, cur : sqlite3.Cursor, serie_id : int, season_number : int, episode_number : int, univers_id : int) :
    cur.execute("INSERT INTO Episode_Univers VALUES (?, ?, ?, ?)", (serie_id, season_number, episode_number, univers_id))
    con.commit()

def UnlinkEpisodeUnivers(con : sqlite3.Connection, cur : sqlite3.Cursor, serie_id : int, season_number : int, episode_number : int, univers_id : int) :
    cur.execute("DELETE FROM Episode_Univers WHERE serie_id = ? and season_number = ? and episode_number = ? and univers_id = ?", (serie_id, season_number, episode_number, univers_id))
    con.commit()

def linkSpecialPresentationUnivers(con : sqlite3.Connection, cur : sqlite3.Cursor, special_presentation_id : int, univers_id : int) :
    cur.execute("INSERT INTO Special_presentation_Univers VALUES (?, ?)", (special_presentation_id, univers_id))
    con.commit()

def UnlinkSpecialPresentationUnivers(con : sqlite3.Connection, cur : sqlite3.Cursor, special_presentation_id : int, univers_id : int) :
    cur.execute("DELETE FROM Special_presentation_Univers WHERE special_presentation_id = ? and univers_id = ?", (special_presentation_id, univers_id))
    con.commit()

def linkOneShotUnivers(con : sqlite3.Connection, cur : sqlite3.Cursor, one_shot_id : int, univers_id : int) :
    cur.execute("INSERT INTO One_shot_Univers VALUES (?, ?)", (one_shot_id, univers_id))
    con.commit()

def UnlinkOneShotUnivers(con : sqlite3.Connection, cur : sqlite3.Cursor, one_shot_id : int, univers_id : int) :
    cur.execute("DELETE FROM One_shot_Univers WHERE one_shot_id = ? and univers_id = ?", (one_shot_id, univers_id))
    con.commit()

# Watched

def addUser(con : sqlite3.Connection, cur : sqlite3.Cursor, name : str) :
    cur.execute("INSERT INTO User VALUES (? ,?)", (None, name))
    con.commit()
    
def rmUser(con : sqlite3.Connection, cur : sqlite3.Cursor, user_id : int) -> None :
    cur.execute("DELETE FROM User WHERE user_id = ?", (user_id,))
    con.commit()

def watchFilm(con : sqlite3.Connection, cur : sqlite3.Cursor, film_id : int, user_id : int) :
    cur.execute("INSERT INTO Watched_film VALUES (?, ?)", (film_id, user_id))
    con.commit()

def unwatchFilm(con : sqlite3.Connection, cur : sqlite3.Cursor, film_id : int, user_id : int) :
    cur.execute("DELETE FROM Watched_Film WHERE film_id = ? and user_id = ?", (film_id, user_id))
    con.commit()

def watchEpisode(con : sqlite3.Connection, cur : sqlite3.Cursor, serie_id : int, season_number : int, episode_number : int, user_id : int) :
    cur.execute("INSERT INTO Watched_Episode VALUES (?, ?, ?, ?)", (serie_id, season_number, episode_number, user_id))
    con.commit()

def unwatchEpisode(con : sqlite3.Connection, cur : sqlite3.Cursor, serie_id : int, season_number : int, episode_number : int, user_id : int) :
    cur.execute("DELETE FROM Watched_Episode WHERE serie_id = ? and season_number = ? and episode_number = ? and user_id = ?", (serie_id, season_number, episode_number, user_id))
    con.commit()

def watchSpecialPresentation(con : sqlite3.Connection, cur : sqlite3.Cursor, special_presentation_id : int, user_id : int) :
    cur.execute("INSERT INTO Watched_Special_presentation VALUES (?, ?)", (special_presentation_id, user_id))
    con.commit()

def unwatchSpecialPresentation(con : sqlite3.Connection, cur : sqlite3.Cursor, special_presentation_id : int, user_id : int) :
    cur.execute("DELETE FROM Watched_Special_presentation WHERE special_presentation_id = ? and user_id = ?", (special_presentation_id, user_id))
    con.commit()

def watchOneShot(con : sqlite3.Connection, cur : sqlite3.Cursor, one_shot_id : int, user_id : int) :
    cur.execute("INSERT INTO Watched_One_shot VALUES (?, ?)", (one_shot_id, user_id))
    con.commit()

def unwatchOneShot(con : sqlite3.Connection, cur : sqlite3.Cursor, one_shot_id : int, user_id : int) :
    cur.execute("DELETE FROM Watched_One_shot WHERE one_shot_id = ? and user_id = ?", (one_shot_id, user_id))
    con.commit()