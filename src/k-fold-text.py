from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from constants import categories
from k_fold_accuracy import k_fold_accuracy
import pickle

x=[]
y={}
yn={}


def main():
	f=open("status.txt","w")
	f.write("Processing started\n");
	f.close()
	for category in categories:
		y[category]=[]
	for n in range(2,11):
		#print('n=',n)
		
		f=open("status.txt","a")
		f.write(str(n)+'\n')
		f.close()
		x.append(n)
		yn=k_fold_accuracy(n)
		pickle.dump(yn,open(str(n)+'.bin','wb'))
		for category in categories:
			y[category].append(yn[category])
		f=open("status.txt","a")
		f.write("completed\n")
		f.close()

	total=[]
	for n in range(len(x)):
		total.append(0)
		for category in categories:
			total[n]+=y[category][n]
		total[n]=total[n]/float(len(categories))
	
	
if __name__ == "__main__":
	exit(main())
