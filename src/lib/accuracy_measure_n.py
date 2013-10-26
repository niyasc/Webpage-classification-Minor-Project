from sys import path
from sys import exit
from os import system
from construct_train_set import construct_train_set
from constants import categories
from clean import getList
from naive_bayes import naive_bayes

def accuracy_measure_n(n):
	x=[]
	y={}
	
	construct_train_set(n)
	
	
	for category in categories:
		system("ls ./webpages/"+category+">.tmp")
		system("head -n "+str(500-n)+" .tmp > .temp")
		a=open(".temp")
		files=a.read()
		a.close()
		files=files.split('\n')
		files.pop()
		cp=0
		documents=0
		for file in files:
			
			terms=getList("webpages/"+category+"/"+file)
			p_cat=naive_bayes(terms)
							
			documents+=1
			if category==p_cat:
				cp+=1
				#else:
				#	print(file," Expected ",category," Predicted ",p_cat)
				
			accuracy=float(cp)*100/documents
				#print(documents," Category ",category,"Prediction Accuracy = ",accuracy,"%")
		
		y[category]=float(cp)*100/documents
		print(category)
		print('Number of true predictions',cp)
		print('Number of false predictions',500-n-cp)
		print('Total number of documents',500-n)
	
	return y
		
	
