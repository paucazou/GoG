#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende

import datetime
import wp_htm_parser as htm
import sqlite3
import wpparser

def load_raw_data(data: dict) -> list:
    """Takes data returned by wpparser
    and return a list of articles
    with only title, date, content and categories.
    """
    posts = data['posts']
    liste = []
    for p in posts:
        liste.append({
            "title" : p['title'],
            "datetime" : p['pub_date'],
            "content" : p['content'],
            "tag" : p['categories'],
            "author" : p['creator'],
            })

    return liste

def to_epoch(data : list) -> list:
    """Takes a list of raw data returned by load_raw_data
    and modifies the date to transform it 
    into a number of seconds from epoch"""
    for elt in data:
        elt.datetime = datetime.datetime.strptime(d,"%a, %d %b %Y %H:%M:%S %z").timestamp()
    return data

def format_content(data : list,formatter=htm.parser()) -> list:
    """Changes the Html content to a 
    gemini friendly content"""
    for elt in data:
        elt.content = formatter(elt.content)
    return data

def format_tags(data: list) -> list:
    """Format categories into tags readable by GoG"""
    data.tag = " ".join([elt.replace(' ','_') for elt in data.tag])
    return data

def from_wp_to_db(filename,db="wp.db"):
    """Takes a WP export file, loads and parses it
    and save its content into db"""
    # load data
    data = wpparser.parses(filename)
    raw_data = load_raw_data(data)
    # format
    articles = to_epoch(raw_data)
    articles = format_content(articles)
    articles = format_tags(articles)
    # save it into database
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    for elt in articles:
        cur.execute("INSERT INTO articles (datetime, author, title, content, tag) VALUES (?, ?, ?, ?, ?)",
                (elt['datetime'], elt['author'], elt['title'], elt['content'],elt['tag']))




