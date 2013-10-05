from os import system
from clean import *
from database import *

categories=["Technology"]
for category in categories:
	system("ls ../webpages/"+category+">.tmp")
	a=open(".tmp")
	files=a.read()
	a.close()
	files=files.split('\n')
	files.pop()
	i=1
	for page in files:
		#print(page)
		
		system("clear")
		print("Category ",category)
		print("File name ",page)
		pwords=getList("../webpages/"+category+"/"+page)
		print("-------------------------------------------------------\n\n")
		resp=input("Is it okey ? ")
		if resp=='n':
			system("rm ../webpages/"+category+"/"+page)
