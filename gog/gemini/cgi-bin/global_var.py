#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
import os.path as op
import pathlib

CGI_DIR = pathlib.Path(__file__).parent.absolute()

DEBUG = True
DB_NAME = "gog.db"
DB_PATH = f"{CGI_DIR}/{DB_NAME}"
