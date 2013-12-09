from sys import path
from sys import exit
from os import system
from construct_train_set import construct_train_set
from constants import categories
from clean import getList
from random import randint
from decimal import Decimal
def naive_bayes(freq_list,database,t):
	#database=pickle.load(open('database.db','rb'))
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
		pc[category]*=Decimal(t)
				
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

def accuracy_measure_n(n):
	'''n->number of train documents'''
	x=[]
	y={}
	documents={}
	accuracy={}
	for category in categories:
		system("ls ./dataset/"+category+">.tmp")
		a=open(".tmp")
		files=a.read()
		a.close()
		files=files.split('\n')
		files.pop()
		documents[category]=files
		accuracy[category]=0
	
	for i in range(0,5):
		print("n=",n,"i=",i)
		train_set={}
		test_set={}
		for category in categories:
			train_set[category]=[]
			test_set[category]=[]
			for j in range(0,n):
				t=documents[category][randint(0,len(documents[category])-1)]
				#print(type(t))
				if t not in train_set[category]:
					train_set[category].append(t)
			for d in documents[category]:
				if d not in train_set[category]:
					test_set[category].append(d)
		print("Traing and test sets created")
		#train the model
		database={}
		#number of train documents nt
		nt=0
		for category in categories:
			database[category]={}
			nt+=len(train_set[category])
			for document in train_set[category]:
				freq=getList('./dataset/'+category+'/'+document)
				for word in freq:
					if word not in database[category]:
						database[category][word]=freq[word]
					else:
						database[category][word]+=freq[word]
		print("training completed n,i",n,i)		
#test model
		#number of train documents
		for category in categories:
			p=0
			j=0;
			t=len(train_set[category])/float(nt)
			for document in test_set[category]:
				j+=1
				freq=getList('./dataset/'+category+'/'+document)
				p_cat=naive_bayes(freq,database,t)
				if p_cat==category:
					p+=1
			f=open("status.txt","a")
			f.write('n='+str(n)+'round'+str(i)+'\n'+str(p)+'documents classified successfully out of '+str(j)+'documents in category'+category+'\n')
			f.close()
				
			
			accuracy[category]+=p*100/len(test_set[category])
	f=open("status.txt","a")
	for category in categories:
		accuracy[category]=accuracy[category]/5
		f.write("accuracy["+category+"]="+str(accuracy[category]));
	f.close()
	print(accuracy)
	return accuracy
