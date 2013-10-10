from sys import path
from sys import exit
from os import system
from construct_train_set1 import construct_train_set
from constants import categories
from predict_category import getCategory

def accuracy_measure_n(n):
	x=[]
	y={}
	
	construct_train_set(n)
	
	
	for category in categories:
		system("ls ./webpages/"+category+">.tmp")
		system("tail -n 500 .tmp > .temp")
		a=open(".temp")
		files=a.read()
		a.close()
		files=files.split('\n')
		files.pop()
		cp=0
		documents=0
		for file in files:
			try:
				p_cat=getCategory("webpages/"+category+"/"+file)
			
			
				documents+=1
				if category==p_cat:
					cp+=1
				else:
					print("Expected ",category," Predicted ",p_cat)
				
				accuracy=float(cp)*100/documents
				print(documents," Category ",category,"Prediction Accuracy = ",accuracy,"%")
			except:
				print(file," makes problem")
		y[category]=float(cp)*100/documents
	
	return y
		
	
