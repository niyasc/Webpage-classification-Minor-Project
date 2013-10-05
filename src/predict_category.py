from sys import path
from sys import exit
path.insert(0, './lib')
from clean import getList
from naive_bayes import naive_bayes

page=input("Enter webpage to predict category ")
freq=getList(page)
print("Given page belongs to "+naive_bayes(freq))
