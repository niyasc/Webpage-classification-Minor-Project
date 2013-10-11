from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from web import *
from functions import *
from naive_bayes1 import *

def main():
	url=input("Enter url : ")
	testpage=WebPage(url)
	text=testpage.getPureText()
	#text=testpage.getImportantContent()
	words=seperateWords(text)
	words=convertToLower(words) # convert words to lowercase
	words=applyStemming(words)
	words=removeStopWords(words) # remove stop words
	freq=genFreqDict(words)
	
	freq=removeAnom(freq)
	print("Category of webpage is ",naive_bayes(freq))
	
	
if __name__ == "__main__":
	exit(main())
