import re
import nltk
from collections import OrderedDict
from nltk import PorterStemmer
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer 

def lemmatize(tokens): 
	# lemmatize words. try both noun and verb lemmatizations 
	lmtzr = WordNetLemmatizer() 
	for i in range(0,len(tokens)): 
		res = lmtzr.lemmatize(tokens[i]) 
		if res == tokens[i]: 
			tokens[i] = lmtzr.lemmatize(tokens[i], 'v') 
		else: 
			tokens[i] = res 
	return tokens





def seperateWords(text):
	'''
		take string into input and return a list of words seperated by digits,non-ascii 		characters,escape sequences,..etc
	'''
	#print('input text',text)
	text=re.sub("\d+|\?|[^a-zA-Z ]", " ", text)
	words=re.findall(r"[\w']+",text.lower())
	#print('words',words)
	return words
	#return nltk.word_tokenize(text) //Avoiding due to presence of un significant words
	

def removeStopWords(words):
	'''
		input : words=>List of words
		output : words=>List of words after removing stop words
	'''
	stop_words=stopwords.words('english')
	s=['home','mail','admin','contact','copright','rights','reserve','sitemap']
	stop_words+=s
	
	for a in stop_words:
		while a in words:
			words.remove(a)
	#print('after removing stop words',words)
	return words

def applyStemming(words):
	'''
		input: words=>List of words
		output: temp=>List of stemmed words
	'''
	temp=lemmatize(words)
	return temp
	
def genFreqDict(words):
	'''
		input : words=>List of words
		output : freq=>Dictionary containing frequency of each words
	'''
	words.sort()
	freq=OrderedDict()
	for word in words:
		if word in freq:
			freq[word]+=1
		else:
			freq[word]=1
	#print('frequency list',freq)
	return freq


def removeSmallWords(words):
	'''
		remove words having length less than 3
	'''
	t=[]
	for word in words:
		if len(word)>2:
			t.append(word)
	return t


