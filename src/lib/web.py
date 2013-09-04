import urllib
import re
from bs4 import BeautifulSoup
class web:
	def getContent(self,address):
		myurl = urllib.urlopen(address)
		source = myurl.read()
		return source
		
	def removeHtml(self,data):
		tags=re.compile(r'<.*?>')
		return tags.sub('',data)
		
	def removeCss(self,data):
		css=re.compile(r'<style.*?/style>')
		return css.sub('',data);
	
	def removeScripts(self,data):
		script=re.compile(r'<script.*?/script>')
		#function=re.compile(r'{.*?}')
		data=script.sub('',data)
		#data=function.sub('',data)
		return data 
		
	def getPureText(self,data):
		data=self.removeHtml(data)
		data=self.removeCss(data)
		data=self.removeScripts(data)
		data=BeautifulSoup(data)
		return data
