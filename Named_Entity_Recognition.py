#!/usr/bin/env python3
#Part of my Conference Project of "Empowering voters with knowledge on politicians via web mining" presented at The 2013 Bicoastal Data Conference at Stanford University on Analyzing money's influence in politics on Feb 2nd, 2013
# This program will report a list of corporations associated with a given politician based on-
# 1) crawls Wikipedia for a given US politician.
# 2) utilizes Named Entity Recognition in advanced NLP to report corporations mentioned in his/her wiki

from webscraping import common, download
from bs4 import BeautifulSoup
import spacy

nlp = spacy.load("en_core_web_sm")

def politician_and_org(politician_name):
    wiki_url = 'http://en.wikipedia.org/wiki/%s' %'_'.join(politician_name.split())
    html = download.Download().fetch(wiki_url)
    html = common.remove_tags(BeautifulSoup(html, "lxml").text)
    html = " ".join(html.split()).lower()

    doc = nlp(html)
    return doc.ents

#Examples
politicians = ['Rand Paul', 'Donald Trump', 'Hillary Rodham Clinton']
for politician in sorted(politicians):
    entities = politician_and_org(politician)
    print('--------- %s ---------' %politician)
    for item in sorted(set([X.text for X in entities if X.label_ in ['ORG', 'MONEY']])):
        print(item)
