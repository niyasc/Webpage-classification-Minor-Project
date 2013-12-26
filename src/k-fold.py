from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from constants import categories
import pylab

x=[]
y={}
ym={}


def main():
	data={2: {'sci.space': 85.7, 'sci.electronics': 53.6, 'comp.windows.x': 80.5, 'rec.motorcycles': 80.6, 'misc.forsale': 64.0, 'comp.sys.mac.hardware': 67.0, 'alt.atheism': 73.1, 'sci.med': 81.8, 'rec.autos': 77.1, 'rec.sport.baseball': 85.0, 'rec.sport.hockey': 95.0, 'talk.politics.guns': 72.4, 'talk.religion.misc': 54.1, 'comp.os.ms-windows.misc': 43.6, 'talk.politics.misc': 77.3, 'talk.politics.mideast': 97.7, 'comp.sys.ibm.pc.hardware': 69.8, 'comp.graphics': 79.4, 'sci.crypt': 95.0, 'soc.religion.christian': 97.3}, 3: {'sci.space': 89.7, 'sci.electronics': 59.4, 'comp.windows.x': 84.6, 'rec.motorcycles': 84.5, 'misc.forsale': 65.6, 'comp.sys.mac.hardware': 69.6, 'alt.atheism': 74.5, 'sci.med': 84.5, 'rec.autos': 79.3, 'rec.sport.baseball': 87.5, 'rec.sport.hockey': 96.7, 'talk.politics.guns': 72.8, 'talk.religion.misc': 51.5, 'comp.os.ms-windows.misc': 49.4, 'talk.politics.misc': 82.8, 'talk.politics.mideast': 98.0, 'comp.sys.ibm.pc.hardware': 73.2, 'comp.graphics': 85.3, 'sci.crypt': 96.8, 'soc.religion.christian': 98.4}, 4: {'sci.space': 89.6, 'sci.electronics': 61.2, 'comp.windows.x': 85.8, 'rec.motorcycles': 85.1, 'misc.forsale': 65.2, 'comp.sys.mac.hardware': 72.9, 'alt.atheism': 72.9, 'sci.med': 89.2, 'rec.autos': 81.4, 'rec.sport.baseball': 87.9, 'rec.sport.hockey': 97.2, 'talk.politics.guns': 73.3, 'talk.religion.misc': 51.5, 'comp.os.ms-windows.misc': 51.6, 'talk.politics.misc': 80.2, 'talk.politics.mideast': 97.8, 'comp.sys.ibm.pc.hardware': 73.4, 'comp.graphics': 87.8, 'sci.crypt': 97.1, 'soc.religion.christian': 98.2}, 5: {'sci.space': 91.1, 'sci.electronics': 62.7, 'comp.windows.x': 84.5, 'rec.motorcycles': 86.0, 'misc.forsale': 67.1, 'comp.sys.mac.hardware': 73.1, 'alt.atheism': 71.2, 'sci.med': 89.1, 'rec.autos': 82.5, 'rec.sport.baseball': 88.7, 'rec.sport.hockey': 97.4, 'talk.politics.guns': 75.8, 'talk.religion.misc': 52.9, 'comp.os.ms-windows.misc': 50.4, 'talk.politics.misc': 81.6, 'talk.politics.mideast': 98.8, 'comp.sys.ibm.pc.hardware': 74.8, 'comp.graphics': 87.6, 'sci.crypt': 96.7, 'soc.religion.christian': 98.4}, 6: {'sci.space': 91.2, 'sci.electronics': 63.0, 'comp.windows.x': 84.8, 'rec.motorcycles': 86.4, 'misc.forsale': 67.2, 'comp.sys.mac.hardware': 72.7, 'alt.atheism': 72.7, 'sci.med': 89.6, 'rec.autos': 82.1, 'rec.sport.baseball': 88.8, 'rec.sport.hockey': 96.9, 'talk.politics.guns': 76.3, 'talk.religion.misc': 50.8, 'comp.os.ms-windows.misc': 52.6, 'talk.politics.misc': 82.1, 'talk.politics.mideast': 97.8, 'comp.sys.ibm.pc.hardware': 74.6, 'comp.graphics': 87.8, 'sci.crypt': 96.6, 'soc.religion.christian': 98.5}, 7: {'sci.space': 90.2, 'sci.electronics': 65.7, 'comp.windows.x': 84.9, 'rec.motorcycles': 86.5, 'misc.forsale': 67.3, 'comp.sys.mac.hardware': 74.0, 'alt.atheism': 73.0, 'sci.med': 89.7, 'rec.autos': 82.2, 'rec.sport.baseball': 88.4, 'rec.sport.hockey': 96.7, 'talk.politics.guns': 76.1, 'talk.religion.misc': 50.6, 'comp.os.ms-windows.misc': 51.9, 'talk.politics.misc': 81.9, 'talk.politics.mideast': 97.6, 'comp.sys.ibm.pc.hardware': 74.7, 'comp.graphics': 87.9, 'sci.crypt': 96.1, 'soc.religion.christian': 98.2}, 8: {'sci.space': 90.5, 'sci.electronics': 65.8, 'comp.windows.x': 85.7, 'rec.motorcycles': 86.8, 'misc.forsale': 67.2, 'comp.sys.mac.hardware': 74.2, 'alt.atheism': 73.3, 'sci.med': 89.9, 'rec.autos': 82.5, 'rec.sport.baseball': 89.3, 'rec.sport.hockey': 97.2, 'talk.politics.guns': 76.7, 'talk.religion.misc': 50.2, 'comp.os.ms-windows.misc': 55.2, 'talk.politics.misc': 82.9, 'talk.politics.mideast': 98.3, 'comp.sys.ibm.pc.hardware': 75.6, 'comp.graphics': 88.7, 'sci.crypt': 96.9, 'soc.religion.christian': 98.6}, 9: {'sci.space': 91.5, 'sci.electronics': 67.3, 'comp.windows.x': 86.2, 'rec.motorcycles': 87.5, 'misc.forsale': 67.7, 'comp.sys.mac.hardware': 74.6, 'alt.atheism': 73.2, 'sci.med': 90.2, 'rec.autos': 83.2, 'rec.sport.baseball': 89.5, 'rec.sport.hockey': 97.2, 'talk.politics.guns': 77.3, 'talk.religion.misc': 50.7, 'comp.os.ms-windows.misc': 54.7, 'talk.politics.misc': 83.0, 'talk.politics.mideast': 98.1, 'comp.sys.ibm.pc.hardware': 77.0, 'comp.graphics': 89.8, 'sci.crypt': 96.7, 'soc.religion.christian': 98.6}}
	for category in categories:
		y[category]=[]
		ym[category]=[]
	for n in range(2,10):
		print('n=',n)
		x.append(n)
		for category in categories:
			y[category].append(data[n][category])
			#ym[category].append(datam[n][category])
		

	total=[]
	#totalm=[]
	for n in range(len(x)):
		total.append(0)
		#totalm.append(0)
		for category in categories:
			total[n]+=y[category][n]
			#totalm[n]+=ym[category][n]
		total[n]=total[n]/float(len(categories))
		#totalm[n]=totalm[n]/float(len(categories))
		#print('old',total[n],'modified',totalm[n])
		
		
		
		
		
						
	#Plot graph
	#for item in y:
	#	t=pylab.plot(x,y[item],label=item)
	t=pylab.plot(x,total,label="Traditional Naive Bayes",linewidth=4,linestyle='-',color='red')
	#t=pylab.plot(x,totalm,label="Modified Model",linewidth=4,linestyle='-',color='blue')
	t=pylab.xlabel('Number of train documents')
	t=pylab.ylabel('Classification accuracy %')	
	t=pylab.legend(loc='lower right')
	t=pylab.title('Number of training documents vs accuracy(Random Subset sampling)')
	t=pylab.grid()
	pylab.show()
	
	
if __name__ == "__main__":
	exit(main())
