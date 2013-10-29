from os import system
from construct_train_set import construct_train_set
from constants import categories
from clean import getList
from naive_bayes import naive_bayes
from database import *

def confusion_matrix(k):
	t=int(500/k) #number of documents in a fold
	print('number of documents in a fold=',t)
	dataset={}
	true_predicted={}
	cmatrix={}
	for category in categories:
		system("ls ./webpages/"+category+">.tmp")
		a=open(".tmp")
		files=a.read()
		a.close()
		files=files.split('\n')
		files.pop()
		dataset[category]=files
		true_predicted[category]=0
		cmatrix[category]={}
		for c in categories:
			cmatrix[category][c]=0
	for i in range(0,k):
		print('i=',i)
		train_set={}
		test_set={}
		database={}
		for category in categories:
			train_set[category]=list(dataset[category][0:i*t]+dataset[category][(i+1)*t:500])
			test_set[category]=list(dataset[category][i*t:(i+1)*t])
			database[category]={}
		#print('train-set\n',train_set)
		#print('test-set\n',test_set)
		for category in categories:
			for file in train_set[category]:
				freq=getList("./webpages/"+category+"/"+file)
				for word in freq:
					if word in database[category]:
						database[category][word]+=freq[word]
					else:
						database[category][word]=freq[word]
		
		make_training_set(database)
		print('database created')
		for category in categories:
			for file in test_set[category]:
				freq=getList("./webpages/"+category+"/"+file)
				p_cat=naive_bayes(freq)
				if p_cat==category:
					true_predicted[category]+=1
				cmatrix[category][p_cat]+=1;
			print('k=',k,'i=',i,'category=',category,'true_predicted\n',true_predicted)
	print(true_predicted)
	
	for actual in categories:
		for predicted in categories:
			print('cmatrix[',actual,'][',predicted,']=',cmatrix[actual][predicted]) 
		
		
