from os import system
from database import *
from constants import *
from functions import *
from clean import *
from collections import OrderedDict




def construct_train_set(n):

	database=OrderedDict()
	for category in categories:
		database[category]=OrderedDict()

	for category in categories:
		system("ls ./webpages/"+category+">.tmp")
		system("tail -n "+str(n)+" .tmp > .temp")
		a=open(".temp")
		files=a.read()
		a.close()
		files=files.split('\n')
		files.pop()
		for file  in files:
			#try:
			freq=getList("./webpages/"+category+"/"+file)
			for word in freq:
				if word in database[category]:
					database[category][word]+=freq[word]
				else:
					database[category][word]=freq[word]
			#except:
			#	print(file,"makes problem")
	#prepare database
	make_training_set(database)
	#print("Training set created")
