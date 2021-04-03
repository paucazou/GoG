#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende

"""Summary of the blog"""
import datetime
import sqlite3
import sys
import urllib.parse as up

print("20 text/gemini")

def generate_articles_list(number) -> str:
    """Generates the list of articles
    with number as maximum"""
    conn = sqlite3.connect('../gog.db')
    cur = conn.cursor()
    cur.execute(""" SELECT title, datetime FROM articles ORDER BY datetime DESC
            WHERE datetime < date('now') LIMIT (?)""",(number,))
    print([elt for elt in cur])
    
text = """
20 text/gemini
{generate_articles_list}
"""
