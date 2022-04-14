import sqlite3

def establish_connection():
    conn = sqlite3.connect('movies.db')
    return conn

def create_database():
    conn = establish_connection()
    c = conn.cursor()
    c.execute("CREATE TABLE movies ( \
        id INTEGER PRIMARY KEY, \
        title TEXT, \
        year INTEGER, \
        director TEXT, \
        actor TEXT \
    )")
    conn.commit()
    conn.close()

def insert_moives():
    conn = establish_connection()
    c = conn.cursor()
    c.executemany("INSERT INTO movies (title, year, director, actor) \
        VALUES (?, ?, ?, ?)",movies_list)
    c.commit()
    c.close()

def fetch_based_on_actor():
    conn = establish_connection()
    c = conn.cursor()
    print(c.execute("SELECT * from movies WHERE actor = 'Christian Bale'").fetchall())

def fetch_movies_table():
    conn = establish_connection()
    c = conn.cursor()
    print(c.execute("Select * from MOVIES").fetchall())


if __name__ == 'main':
    establish_connection()
    create_database()
    movies_list = [("The Shawshank redumption", 1994, "Frank Darabont", "Tim Robbins"),("The Godfather", 1972, "Francis Ford Coppola", "Marlon Brando"),
    ("The Godfather: Part II", 1974, "Francis Ford Coppola", "Al Pacino"),
    ("The Dark Knight", 2008, "Christopher Nolan", "Christian Bale"),("3 idiots","2009","Rajkumar Hirani","Aamir Khan"),
    ("Inception","2010","Christopher Nolan","Leonardo DiCaprio"),
    ("The Dark Knight Rises","2012","Christopher Nolan","Christian Bale"),
    ("Pulp Fiction","1994","Quentin Tarantino","John Travolta")]
    fetch_based_on_actor()
    fetch_movies_table()


