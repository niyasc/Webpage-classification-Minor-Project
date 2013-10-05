import urllib
import nltk
import re

class WebSite:
	
	def __init__(self,address):
		self.content=self.getContent(address)
	
	def getContent(self,address):
		response = urllib.urlopen(address)
		data=response.read()      # a `bytes` object
		text=data.decode('utf-8') # a `str`; this step can't be used if data is binary
		return text
		
	def removeHtml(self,data):
		html=re.compile(r'(?is)<.*?>')
		return html.sub(' ',data)
		
	def removeCss(self,data):
		css=re.compile(r"(?is)<style[^>]*>(.*?)</style>")
		return css.sub(' ',data);
	
	def removeScripts(self,data):
		script=re.compile(r"(?is)<script[^>]*>(.*?)</script>")
		#function=re.compile(r'{.*?}')
		data=script.sub(' ',data)
		#data=function.sub('',data)
		return data 
		
	def getPureHtml(self):

		data=self.removeCss(self.content)
		data=self.removeScripts(data)
		#data=BeautifulSoup(data)
		return data
		
	def getPureText(self):
		'''data=self.removeCss(self.content)
		data=self.removeScripts(data)
		data=self.removeHtml(data)
		#soup=BeautifulSoup(data)
		#return soup.get_text()
		return data'''
		return nltk.clean_html(self.content)
	
	def getTitle(self):
		
		title=re.findall(r"(?is)<title[^>]*>(.*?)</title>",self.getPureHtml())
		return list(title)[0]
		
class HtmlFile:
	
	def __init__(self,fname):
		a=open(fname)
		self.content=a.read()
		a.close()
		self.content=str(self.content.encode('utf-8','ignore'))
		
	def removeHtml(self,data):
		html=re.compile(r'(?is)<.*?>')
		return html.sub(' ',data)
		
	def removeCss(self,data):
		css=re.compile(r"(?is)<style[^>]*>(.*?)</style>")
		return css.sub(' ',data);
	
	def removeScripts(self,data):
		script=re.compile(r"(?is)<script[^>]*>(.*?)</script>")
		#function=re.compile(r'{.*?}')
		data=script.sub(' ',data)
		#data=function.sub('',data)
		return data 
		
	def getPureHtml(self):

		data=self.removeCss(self.content)
		data=self.removeScripts(data)
		#data=BeautifulSoup(data)
		return data
		
	def getPureText(self):
		'''data=self.removeCss(self.content)
		data=self.removeScripts(data)
		data=self.removeHtml(data)
		#soup=BeautifulSoup(data)
		#return soup.get_text()
		return data'''
		return nltk.clean_html(self.content)
	
	def getTitle(self):
		
		title=re.findall(r"(?is)<title[^>]*>(.*?)</title>",self.getPureHtml())
		return list(title)[0]
