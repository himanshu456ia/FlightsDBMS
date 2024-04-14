import sqlite3
passengers_db = "Databases/passengers.db"

def init_db():
    con = sqlite3.connect(passengers_db)
    cur = con.cursor()