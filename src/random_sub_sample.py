from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from constants import categories
import pylab

x=[]
y={}
yn={}


def main():
	data={400: {'sci.med': 89.66666666666667, 'comp.graphics': 84.94444444444444, 'talk.politics.mideast': 98.8888888888889, 'rec.autos': 82.0, 'comp.sys.mac.hardware': 70.72222222222223, 'soc.religion.christian': 98.26912339475153, 'talk.politics.guns': 83.61111111111113, 'rec.sport.hockey': 96.66666666666667, 'sci.electronics': 64.33333333333333, 'talk.religion.misc': 47.333333333333336, 'comp.os.ms-windows.misc': 56.388888888888886, 'alt.atheism': 83.88888888888887, 'sci.crypt': 98.5, 'talk.politics.misc': 77.33333333333333, 'misc.forsale': 63.666666666666664, 'comp.sys.ibm.pc.hardware': 76.83333333333333, 'comp.windows.x': 88.5, 'rec.motorcycles': 79.27777777777777, 'rec.sport.baseball': 88.88888888888887, 'sci.space': 94.0}, 600: {'sci.med': 90.75, 'comp.graphics': 94.25, 'talk.politics.mideast': 98.0, 'rec.autos': 83.08333333333333, 'comp.sys.mac.hardware': 74.41666666666667, 'soc.religion.christian': 99.07640638119229, 'talk.politics.guns': 82.58333333333333, 'rec.sport.hockey': 97.5, 'sci.electronics': 66.33333333333333, 'talk.religion.misc': 60.333333333333336, 'comp.os.ms-windows.misc': 63.833333333333336, 'alt.atheism': 72.33333333333333, 'sci.crypt': 98.25, 'talk.politics.misc': 85.0, 'misc.forsale': 66.41666666666667, 'comp.sys.ibm.pc.hardware': 77.33333333333333, 'comp.windows.x': 85.83333333333333, 'rec.motorcycles': 86.33333333333333, 'rec.sport.baseball': 93.0, 'sci.space': 93.41666666666667}, 700: {'sci.med': 91.66666666666667, 'comp.graphics': 92.66666666666667, 'talk.politics.mideast': 99.33333333333333, 'rec.autos': 83.77777777777779, 'comp.sys.mac.hardware': 79.1111111111111, 'soc.religion.christian': 98.989898989899, 'talk.politics.guns': 82.33333333333333, 'rec.sport.hockey': 98.22222222222223, 'sci.electronics': 71.44444444444444, 'talk.religion.misc': 51.11111111111111, 'comp.os.ms-windows.misc': 60.77777777777777, 'alt.atheism': 80.0, 'sci.crypt': 98.0, 'talk.politics.misc': 83.11111111111113, 'misc.forsale': 63.555555555555564, 'comp.sys.ibm.pc.hardware': 78.22222222222223, 'comp.windows.x': 87.55555555555556, 'rec.motorcycles': 89.0, 'rec.sport.baseball': 91.33333333333333, 'sci.space': 92.66666666666667}, 100: {'sci.med': 68.29629629629629, 'comp.graphics': 59.370370370370374, 'talk.politics.mideast': 92.8888888888889, 'rec.autos': 56.03703703703704, 'comp.sys.mac.hardware': 67.11111111111111, 'soc.religion.christian': 94.42586399108137, 'talk.politics.guns': 55.77777777777777, 'rec.sport.hockey': 88.0, 'sci.electronics': 40.333333333333336, 'talk.religion.misc': 36.333333333333336, 'comp.os.ms-windows.misc': 30.962962962962962, 'alt.atheism': 78.14814814814815, 'sci.crypt': 87.18518518518518, 'talk.politics.misc': 81.48148148148148, 'misc.forsale': 59.96296296296296, 'comp.sys.ibm.pc.hardware': 53.96296296296296, 'comp.windows.x': 64.14814814814815, 'rec.motorcycles': 76.37037037037038, 'rec.sport.baseball': 84.55555555555556, 'sci.space': 76.03703703703702}, 200: {'sci.med': 83.0, 'comp.graphics': 90.70833333333333, 'talk.politics.mideast': 94.20833333333333, 'rec.autos': 68.54166666666667, 'comp.sys.mac.hardware': 51.583333333333336, 'soc.religion.christian': 99.24717691342535, 'talk.politics.guns': 70.75, 'rec.sport.hockey': 92.5, 'sci.electronics': 42.125, 'talk.religion.misc': 51.833333333333336, 'comp.os.ms-windows.misc': 34.625, 'alt.atheism': 66.29166666666667, 'sci.crypt': 98.0, 'talk.politics.misc': 85.125, 'misc.forsale': 55.083333333333336, 'comp.sys.ibm.pc.hardware': 67.20833333333333, 'comp.windows.x': 73.54166666666667, 'rec.motorcycles': 77.625, 'rec.sport.baseball': 87.5, 'sci.space': 88.58333333333333}, 500: {'sci.med': 92.33333333333333, 'comp.graphics': 91.86666666666667, 'talk.politics.mideast': 98.26666666666667, 'rec.autos': 83.33333333333333, 'comp.sys.mac.hardware': 67.2, 'soc.religion.christian': 99.19517102615696, 'talk.politics.guns': 78.46666666666667, 'rec.sport.hockey': 96.2, 'sci.electronics': 70.73333333333333, 'talk.religion.misc': 53.93333333333333, 'comp.os.ms-windows.misc': 61.53333333333333, 'alt.atheism': 76.33333333333334, 'sci.crypt': 96.53333333333335, 'talk.politics.misc': 84.60000000000001, 'misc.forsale': 67.2, 'comp.sys.ibm.pc.hardware': 77.0, 'comp.windows.x': 85.33333333333333, 'rec.motorcycles': 88.26666666666667, 'rec.sport.baseball': 91.66666666666667, 'sci.space': 92.39999999999999}, 900: {'sci.med': 94.33333333333333, 'comp.graphics': 90.0, 'talk.politics.mideast': 98.0, 'rec.autos': 87.66666666666667, 'comp.sys.mac.hardware': 82.33333333333333, 'soc.religion.christian': 100.0, 'talk.politics.guns': 82.66666666666667, 'rec.sport.hockey': 96.66666666666667, 'sci.electronics': 78.33333333333333, 'talk.religion.misc': 49.333333333333336, 'comp.os.ms-windows.misc': 59.333333333333336, 'alt.atheism': 75.66666666666667, 'sci.crypt': 98.0, 'talk.politics.misc': 85.0, 'misc.forsale': 71.0, 'comp.sys.ibm.pc.hardware': 81.66666666666667, 'comp.windows.x': 93.0, 'rec.motorcycles': 92.66666666666667, 'rec.sport.baseball': 92.0, 'sci.space': 95.33333333333333}, 300: {'sci.med': 90.66666666666667, 'comp.graphics': 81.33333333333333, 'talk.politics.mideast': 98.09523809523809, 'rec.autos': 76.90476190476191, 'comp.sys.mac.hardware': 68.76190476190476, 'soc.religion.christian': 98.99569583931134, 'talk.politics.guns': 75.95238095238095, 'rec.sport.hockey': 94.33333333333333, 'sci.electronics': 56.666666666666664, 'talk.religion.misc': 43.52380952380952, 'comp.os.ms-windows.misc': 47.28571428571428, 'alt.atheism': 77.90476190476191, 'sci.crypt': 98.28571428571428, 'talk.politics.misc': 82.33333333333333, 'misc.forsale': 61.47619047619048, 'comp.sys.ibm.pc.hardware': 77.09523809523809, 'comp.windows.x': 84.3809523809524, 'rec.motorcycles': 80.3809523809524, 'rec.sport.baseball': 84.80952380952381, 'sci.space': 88.85714285714285}, 800: {'sci.med': 93.33333333333333, 'comp.graphics': 92.0, 'talk.politics.mideast': 98.66666666666667, 'rec.autos': 85.66666666666667, 'comp.sys.mac.hardware': 80.5, 'soc.religion.christian': 98.8155668358714, 'talk.politics.guns': 79.5, 'rec.sport.hockey': 98.0, 'sci.electronics': 76.16666666666667, 'talk.religion.misc': 52.333333333333336, 'comp.os.ms-windows.misc': 63.833333333333336, 'alt.atheism': 78.16666666666667, 'sci.crypt': 97.16666666666667, 'talk.politics.misc': 87.5, 'misc.forsale': 70.5, 'comp.sys.ibm.pc.hardware': 76.83333333333333, 'comp.windows.x': 92.0, 'rec.motorcycles': 88.5, 'rec.sport.baseball': 91.83333333333333, 'sci.space': 93.83333333333333}}


	for category in categories:
		y[category]=[]
	for n in range(100,1000,100):
		print('n=',n)
		x.append(n)
		for category in categories:
			y[category].append(data[n][category])
		

	total=[]
	for n in range(len(x)):
		total.append(0)
		for category in categories:
			total[n]+=y[category][n]
		total[n]=total[n]/float(len(categories))
		print(total[n])
		
		
		
		
		
						
	#Plot graph
	#for item in y:
	#	t=pylab.plot(x,y[item],label=item)
	t=pylab.plot(x,total,label="Overal performance",linewidth=4,linestyle='-',color='red')
	t=pylab.xlabel('Number of train documents')
	t=pylab.ylabel('Classification accuracy %')	
	t=pylab.legend(loc='lower right')
	t=pylab.title('Number of training documents vs accuracy')
	t=pylab.grid()
	pylab.show()
	
	
if __name__ == "__main__":
	exit(main())
