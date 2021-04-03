#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende

"""This script creates a new sqlite database
if it does not yet exist"""

import os.path as path
import sqlite3
dbname = "../gemini/cgi-bin/gog.db"

def create_db():
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    curs.execute("""CREATE TABLE articles
                (id INTEGER PRIMARY KEY, datetime REAL, author TEXT, title TEXT, content TEXT, tag TEXT)""")
    conn.commit()
    conn.close()

def check_db():
    if path.exists(dbname):
        raise ValueError(f"Database already exists")

    return True

if __name__ == "__main__":
    if check_db():
        create_db()
        print("Db created")



