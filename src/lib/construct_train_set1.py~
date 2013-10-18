from os import system
from database import *
from constants import *
from functions import *
from clean import *
import MySQLdb




def construct_train_set(n):

	database=[]

	for category in categories:
		system("ls ./webpages/"+category+">.tmp")
		system("tail -n "+str(n)+" .tmp > .temp")
		a=open(".temp")
		files=a.read()
		a.close()
		files=files.split('\n')
		files.pop()
		for file  in files:
			try:
				freq=getList("./webpages/"+category+"/"+file)
				freq['_category']=category
				database.append(freq)
			except:
				print(file,"makes problem")
	#prepare database
	make_training_set(database)
	#print("Training set created")
