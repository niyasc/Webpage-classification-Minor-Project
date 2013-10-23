from constants import categories
import pickle
from decimal import Decimal
from collections import OrderedDict

def naive_bayes(freq_list):
	database=pickle.load(open('database.db','rb'))
	#print(database)
	#print(type(database))
	
	v=0	
	for category in categories:
		for word in database[category]:
			v+=database[category][word]
	
	pc={}
	for category in categories:
		attributes=database[category]
		n=0
		for word in attributes:
			n+=attributes[word]
		
		pc[category]=Decimal(10**1000)
		for word in freq_list:
			if word not in attributes:
				pc[category]=pc[category]*Decimal((1.0/(n+v)))
			else:
				pc[category]=pc[category]*Decimal(((1.0+attributes[word])/(n+v)))
				
	'''for category in categories:
		print('Probability of ',category,' ',pc[category])
	'''
	
	Category='Unable to decide'
	p=0
	for category in categories:
		if p<pc[category]:
			Category=category
			p=pc[category]
	
	return Category

