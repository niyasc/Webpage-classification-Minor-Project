from constants import categories
from pymongo import MongoClient
from math import sqrt

e=2.71828
pi=3.141592

def g(xk,meanki,sdki):

	power=-(xk-meanki)**2
	power=power/(2*sdki**2)
	value=pow(e,power)
	value=value/(sqrt(2*pi)*sdki)
	return value

def naive_bayes(freq_list):
	'''
		Find the category corresponding to given frequence list and return category
	'''
	client=MongoClient()
	db=client.train
	training_set=db.training_set
	pc={}
	for category in categories:
		attributes={}
		documents=[]
		for tset in training_set.find({'_category':category}):
			a=tset.pop('_category')
			a=tset.pop('_id')
			documents.append(tset)
		for document in documents:
			for word in document:
				if word not in attributes:
					attributes[word]=document[word]
				else:
					attributes[word]+=document[word]
		number_of_training_documents=len(documents)
		pc[category]=pow(2,1023)
		for word in freq_list:
			if word in attributes:
				meanki=attributes[word]/float(number_of_training_documents)
				varrianceki=0
				for document in documents:
					if word in document:
						varrianceki+=(meanki-document[word])**2
					else:
						varrianceki+=(meanki)**2
				varrianceki=varrianceki/float(number_of_training_documents)
				sdki=sqrt(varrianceki)
				
				if varrianceki!=0:
					pc[category]*=g(freq_list[word],meanki,sdki)
					
	'''for category in categories:
		print("Probability of "+category+" = "+str(pc[category]))
	'''
		
	p=0
	Category='Unable to decide'
	for category in categories:
		if p<pc[category]:
			Category=category
			p=pc[category]
	
	return Category			
			
			
				
	

