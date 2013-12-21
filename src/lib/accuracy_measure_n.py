from sys import path
from sys import exit
from os import system
from construct_train_set import construct_train_set
from constants import categories
from clean import getList
from random import randint
from random import seed
from math import log
import pickle
def naive_bayes(freq_list,database):
	#database=pickle.load(open('database.db','rb'))
	#print(type(database))
	
	v=0	
	for category in categories:
		for word in database[category]:
			v+=database[category][word]
	t=0.0
	for word in freq_list:
		t+=freq_list[word]
			

	
	pc={}
	for category in categories:
		attributes=database[category]
		n=0
		for word in attributes:
			n+=attributes[word]
		
		pc[category]=0
		
		
		
		for word in freq_list:
			print(log(freq_list[word]/t))
			if word not in attributes:
				pc[category]=pc[category]+1.0/(n+v)
			else:
				pc[category]=pc[category]+(1.0+attributes[word]/(n+v))				
	'''for category in categories:
		print('Probability of ',category,' ',pc[category])
	'''
	
	Category='Unable to decide'
	p=-100000
	for category in categories:
		if p<pc[category]:
			Category=category
			p=pc[category]
	
	return Category

def makedb(train_set):
	database={}
	for category in categories:
		database[category]={}
		for document in train_set[category]:
			freq=getList('./dataset/'+category+'/'+document)
			for word in freq:
				if word not in database[category]:
					database[category][word]=freq[word]
				else:
					database[category][word]+=freq[word]
	return database

def accuracy_measure_n(n):
	'''n->number of train documents'''
	seed(0)
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
	
	for i in range(0,3):
		print("n=",n,"i=",i)
		train_set={}
		test_set={}
		for category in categories:
			train_set[category]=[]
			test_set[category]=[]
			for j in range(0,n):
				t=documents[category][randint(0,len(documents[category])-1)]
				#print(type(t))
				while t in train_set[category]:
					t=documents[category][randint(0,len(documents[category])-1)]
				train_set[category].append(t)
			for d in documents[category]:
				if d not in train_set[category]:
					test_set[category].append(d)
		print("Traing and test sets created")
		'''#divide train set into 3
		tset0={}
		tset1={}
		tset2={}
		tset3={}
		tset4={}
		for category in train_set:
			tset0[category]=train_set[category][0:int(n/5)]
			tset1[category]=train_set[category][int(n/5):int(2*n/5)]
			tset2[category]=train_set[category][int(2*n/5):int(3*n/5)]
			tset3[category]=train_set[category][int(3*n/5):int(4*n/5)]
			tset4[category]=train_set[category][int(4*n/5):]
		#train the model
		database0=makedb(tset0)
		database1=makedb(tset1)
		database2=makedb(tset2)
		database3=makedb(tset3)
		database4=makedb(tset4)
		
		print("training completed n,i",n,i)		
#test model
		vp={0:1,1:1,2:1,3:1,4:1}
		#number of train documents'''
		database=makedb(train_set)
		print(database)
		pickle.dump(database,open('database.db','wb'))
		exit()
		for category in categories:
			#vp={0:1,1:1,2:1,3:1,4:1}
			p=0
			j=0;
			for document in test_set[category]:
				j+=1
				freq=getList('./dataset/'+category+'/'+document)
				'''pc={}
				cc={}
				cc[0]=naive_bayes(freq,database0)
				cc[1]=naive_bayes(freq,database1)
				cc[2]=naive_bayes(freq,database2)
				cc[3]=naive_bayes(freq,database3)
				cc[4]=naive_bayes(freq,database4)
				for l in range(0,5):
					#print('classfier',l,'with power ',vp[l],'predicts',cc[l])
					if cc[l] in pc:
						pc[cc[l]]+=vp[l]
					else:
						pc[cc[l]]=vp[l]
				
				#collect majority vote	
				p_cat=max(pc, key=pc.get)
				#print('predicted category',p_cat)
				if p_cat==category:
					p+=1
					
				#change voting power
				for l in range(0,5):
					if cc[l]==category:
						if vp[l]<2:
							vp[l]*=1.01
					else:
						if vp[l]>0.5:
							vp[l]*=0.99
				
				
				#print('n',n,'i',i,'j',j,'accuracy',(p/float(j))*100,'category',category)
				#print("---------------------------------------------------")
			'''
				p_cat=naive_bayes(freq,database)
				if p_cat==category:
					p+=1
				if p_cat=='Unable to decide':
					print("unable to decide happens")
			f=open("status.txt","a")
			f.write('n='+str(n)+'round'+str(i)+'\n'+str(p)+'documents classified successfully out of '+str(j)+'documents in category'+category+'\n')
			f.close()
				
			
			accuracy[category]+=p*100/len(test_set[category])
	f=open("status.txt","a")
	for category in categories:
		accuracy[category]=accuracy[category]/3
		f.write("accuracy["+category+"]="+str(accuracy[category]));
	f.close()
	print(accuracy)
	return accuracy
