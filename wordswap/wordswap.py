
import random
import os
import sys
from nltk.tokenize.regexp import RegexpTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
import re
import pickle

#Tokenizers:

WordListTokenizer = RegexpTokenizer(pattern = ', ', gaps = True, discard_empty = True)
InputTokenizer = TreebankWordTokenizer()

#Tagger:

f = open('WordSwapTagger.pickle', 'rb')
tagger = pickle.load(f)

#wordlists using Treebank tags: jj, jjr, jjs, nn, nns, vb, vbd, vbg, vbn, vbp, vbz

jj = WordListTokenizer.tokenize((open(os.path.join(sys.path[0], 'jj.txt')).read())) 
jjr = WordListTokenizer.tokenize((open(os.path.join(sys.path[0], 'jjr.txt')).read())) 
jjs = WordListTokenizer.tokenize((open(os.path.join(sys.path[0], 'jjs.txt')).read()))
nn = WordListTokenizer.tokenize((open(os.path.join(sys.path[0], 'nn.txt')).read()))
nns = WordListTokenizer.tokenize((open(os.path.join(sys.path[0], 'nns.txt')).read()))
vb = WordListTokenizer.tokenize((open(os.path.join(sys.path[0], 'vb.txt')).read()))
vbd = WordListTokenizer.tokenize((open(os.path.join(sys.path[0], 'vbd.txt')).read()))
vbg = WordListTokenizer.tokenize((open(os.path.join(sys.path[0], 'vbg.txt')).read()))
vbn = WordListTokenizer.tokenize((open(os.path.join(sys.path[0], 'vbn.txt')).read()))
vbp = WordListTokenizer.tokenize((open(os.path.join(sys.path[0], 'vbp.txt')).read()))
vbz = WordListTokenizer.tokenize((open(os.path.join(sys.path[0], 'vbz.txt')).read()))

#original has to be str input

def WordSwap(txt):

    """given an input text, swaps out words with random words with the same POS tags"""
    
    tokens = InputTokenizer.tokenize(txt)
    postags = tagger.tag(tokens)
    newtxt = txt
    stopwords = stopwords.words('english')

    for pos in postags:
        oldword = pos[0]
        oldpattern = '[^a-zA-Z0-9]' + oldword + '[^a-zA-Z0-9]'
        #bypass stopwords
        if oldword not in stopwords:
            #bypass contractions
            if re.search('\w*\'w*', oldword) == None: 
              #ensure the replacement location is a standalone word, not word part.    
                if re.search(oldpattern, newtxt) != None: 
                    location = re.search(oldpattern, newtxt).span()
                    if pos[1] == 'JJ':
                        newword = jj[random.randint(0, len(jj)-1)]
                        newtxt = newtxt[:location[0]+1] + newword + newtxt[(location[1]-1):]
                    if pos[1] == 'JJR':
                        newword = jjr[random.randint(0, len(jjr)-1)]
                        newtxt = newtxt[:location[0]+1] + newword + newtxt[(location[1]-1):]
                    if pos[1] == 'JJS':
                        newword = jjs[random.randint(0, len(jjs)-1)]
                        newtxt = newtxt[:location[0]+1] + newword + newtxt[(location[1]-1):]
                    if pos[1] == 'NN':
                        newword = nn[random.randint(0, len(nn)-1)]
                        newtxt = newtxt[:location[0]+1] + newword + newtxt[(location[1]-1):]
                    if pos[1] == 'NNS':
                        newword = nns[random.randint(0, len(nns)-1)]
                        newtxt = newtxt[:location[0]+1] + newword + newtxt[(location[1]-1):]
                    if pos[1] == 'VB':
                        newword = vb[random.randint(0, len(vb)-1)]
                        newtxt = newtxt[:location[0]+1] + newword + newtxt[(location[1]-1):]
                    if pos[1] == 'VBD':
                        newword = vbd[random.randint(0, len(vbd)-1)]
                        newtxt = newtxt[:location[0]+1] + newword + newtxt[(location[1]-1):]
                    if pos[1] == 'VBG':
                        newword = vbg[random.randint(0, len(vbg)-1)]
                        newtxt = newtxt[:location[0]+1] + newword + newtxt[(location[1]-1):]
                    if pos[1] == 'VBN':
                        newword = vbn[random.randint(0, len(vbn)-1)]
                        newtxt = newtxt[:location[0]+1] + newword + newtxt[(location[1]-1):]
                    if pos[1] == 'VBP':
                        newword = vbp[random.randint(0, len(vbp)-1)]
                        newtxt = newtxt[:location[0]+1] + newword + newtxt[(location[1]-1):]
                    if pos[1] == 'VBZ':
                        newword = vbz[random.randint(0, len(vbz)-1)]
                        newtxt = newtxt[:location[0]+1] + newword + newtxt[(location[1]-1):]
                else:
                    pass
            else:
                pass
        else:
            pass
    return newtxt
	
