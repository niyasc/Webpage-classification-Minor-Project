from constants import categories
import pickle
from decimal import Decimal

def naive_bayes(freq_list):
	database=pickle.load(open('database.db','rb'))
	
	v=0	
	for document in database:
		for word in document:
			if word!='_category':
				v+=document[word]
	
	pc={}
	for category in categories:
		attributes={}
		n=0
		for document in database:
			if document['_category']==category:
				for word in document:
					if word!="_category":
						n+=document[word]
						if word not in attributes:
							attributes[word]=document[word]
						else:
							attributes[word]+=document[word]
		
		pc[category]=pow(2,1023)
		for word in freq_list:
			if word not in attributes:
				pc[category]=pc[category]*(1.0/(n+v))
			else:
				pc[category]=pc[category]*((1.0+attributes[word])/(n+v))
				
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

