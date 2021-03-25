# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:42:43 2020

@author: paulp
"""

from textblob import TextBlob
import io
import random


source = io.open(r'C:\Users\paulp\Desktop\Computing Notes and Projects\wordlists\12dicts-6.0.2\American\6of12.txt', encoding = 'utf-8')
dictionary = TextBlob(source.read())

#io.open doesn't like backslashes followed by numerical digits. 
#can you also run io.open with the "r'" prefix?

source = io.open(r'C:\Users\paulp\Desktop\Computing Notes and Projects\swanns way.txt', encoding = 'utf-8')
INPTXT = TextBlob(source.read())

#encoding errors - for .txt extensions, how can you make sure these are all in utf-8
#without BOM or other encoding? How will they appear when they are converted/encoded/decoded?

def adjfilter(text):
    AdjList = []
    for (word, tag) in text.tags:
        if tag == 'JJ':
            AdjList = AdjList + [word]
    return AdjList

#will strings in AdjList retain their u' prefix when replaced in the source text?
#how will you edit out adjs with special characters '+' and '=' from 6of12dict?   
    


def replaceMultiple(INPTXT, OLDADJ):
    n = 0
    INPADJS = adjfilter(INPTXT)
    DICTADJS = adjfilter(dictionary)
    OLDADJ = INPADJS[n]
    for elem in INPADJS:
        INPTXT = INPTXT.replace(elem, random.choice(DICTADJS))
        n = n + 1
    return INPTXT


