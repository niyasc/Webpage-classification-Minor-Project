import sys
#sys.path.insert(0, './lib') #set library location
from web import *
from functions import *
from cleaner import *



def getWords(fname):
	#print(getList(fname))
	testpage=HtmlFile(fname)
	text=testpage.getPureText()
	print(text)
	text=re.sub("\d+|\?|[^a-zA-Z0-9 ]", " ", text)
	obj=DataClean(text)
	return obj.GetData()
	
