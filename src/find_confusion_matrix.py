from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from constants import categories
from confusion_matrix import confusion_matrix

def main():
	n=int(input("Enter number of folds k : "))
	confusion_matrix(n)
	
	
if __name__ == "__main__":
	exit(main())
