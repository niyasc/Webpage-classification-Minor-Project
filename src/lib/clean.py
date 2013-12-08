import sys
#sys.path.insert(0, './lib') #set library location
from web import *
from functions import *


def getList(fname):
	testpage=HtmlFile(fname)
	text=testpage.getPureText()
	#words = DataClean(text).GetData()
	#text=testpage.getImportantContent()
	words=seperateWords(text)
	words=applyStemming(words)
	words=removeStopWords(words) # remove stop words
	words=removeSmallWords(words)
	freq=genFreqDict(words)
	
	return freq
	#print(freq)
	#print("Number of uniq words : "+str(len(freq)))
	#print("Pure Text")
	#print(testsite.getPureText())
	
