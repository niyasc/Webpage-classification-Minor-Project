from os import system
from clean import *
from database import *
from constants import *
from collections import OrderedDict



def construct_train_set(n):

	database=[]

	for category in categories:
		system("ls ./webpages/"+category+"|sort>.tmp")
		system("head -n "+str(n)+" .tmp > .temp")
		a=open(".temp")
		files=a.read()
		a.close()
		files=files.split('\n')
		files.pop()
		#print(len(files))
		for page in files:
			#print(page)
			#print("\rcategory : "+category+" Document number "+str(i)+" Dictionary created\r")
			try:
				pwords=getList("./webpages/"+category+"/"+page)
				pwords['_category']=category
				database.append(pwords)
			except:
				print(page," makes problem")
	#prepare database
	make_training_set(database)
	#print("Training set created")
