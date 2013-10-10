from sys import path
from sys import exit
from clean import getList
from naive_bayes import naive_bayes

def getCategory(page):
	freq=getList(page)
	return naive_bayes(freq)
