#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende

import html.parser as hp
import re
import unicodedata

class ParserToGem(hp.HTMLParser):
    """Parses html to return a gemini string"""
    tags_to_replace = {
            "h1" : "#",
            "h2" : "##",
            "h3" : "##",
            "blockquote" : "> ",
            "a" : "=> ",
            "br": "\n",
            "li": "*",
            "pre":"```",
            }
    tags_data_to_remove = [
            "img",
            ]
    def __call__(self,raw_data):
        self.raw_data = unicodedata.normalize('NFKC',raw_data)
        self.gem = ""
        self.feed(self.raw_data)
        # handle [caption]
        self.gem = re.sub('\[caption.*\[/caption]','',self.gem)


    def __init__(self):
        super().__init__()
        self.tags = []
        self._save_data = True
        self._is_anchor = False

    def add_newline(self):
        """Add a newline if last character in self.gem is not a newline"""
        if len(self.gem) == 0 or self.gem[-1] == '\n':
            return
        self.gem += "\n"

    def handle_starttag(self,tag,attrs):
        attrs_d = dict(attrs)
        self.tags.append(tag)
        if tag in self.tags_to_replace:
            self._save_data = True
            if tag == 'a' and attrs_d['href'][0] == '#':
                # anchor: gemini doesn't support them
                self._is_anchor = True
                return

            self.add_newline()
            self.gem += self.tags_to_replace[tag] + " "
            if tag == 'a':
                self.gem += attrs_d['href'] + " "

        elif tag in self.tags_data_to_remove:
            self._save_data = False

    def handle_endtag(self,tag):
        self.tags.pop()
        if tag in self.tags_data_to_remove:
            self._save_data = True
        elif tag in self.tags_to_replace and not self._is_anchor:
            self.add_newline()

    def handle_data(self,data):
        if self._save_data is True:
            self.gem += data

parser = ParserToGem

