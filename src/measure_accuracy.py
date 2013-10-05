from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from construct_train_set import construct_train_set
from constants import categories
from predict_category import getCategory
import pylab

def main():
	x=[]
	y={}
	cp=0
	documents=0
	for category in categories:
		y[category]=[]
	for n in range(10,200,200):
		print('n=',n)
		x.append(n)
		construct_train_set(n)
		
		
		
		for category in categories:
			system("ls ./webpages/"+category+">.tmp")
			system("head -n "+str(200-n)+" .tmp > .temp")
			a=open(".temp")
			files=a.read()
			a.close()
			files=files.split('\n')
			files.pop()
			#cp=0
			#documents=0
			for file in files:
				try:
					p_cat=getCategory("webpages/"+category+"/"+file)
				except:
					print("error",file)
					exit()
				documents+=1
				if category==p_cat:
					cp+=1
				else:
					print(file,"Expected ",category," Predicted ",p_cat)
				accuracy=float(cp)*100/documents
				print("Prediction Accuracy = ",accuracy,"%")
			
			y[category].append(float(cp)*100/documents)
		accuracy=float(cp)*100/documents
			
		print("Prediction Accuracy = ",accuracy,"%")
						
	#Plot graph
	for item in y:
		t=pylab.plot(x,y[item],label=item)
	t=pylab.xlabel('Number of trainig documents')
	t=pylab.ylabel('Classification accuracy %')	
	t=pylab.legend(loc='upper right')
	pylab.show()
	
	
if __name__ == "__main__":
	exit(main())
