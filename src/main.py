#!/usr/bin/python3

from gi.repository import Gtk
from sys import path
from sys import exit
from os import system
path.insert(0, './lib') #set library location
from web import *
from functions import *
from naive_bayes1 import *
from urllib.error import HTTPError

class myWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self,title='Hello, World')
		
		self.box1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		self.box2=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		self.box3=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		self.add(self.box1)
		
		self.label1=Gtk.Label('File/URL')
		
		self.input=Gtk.Entry()
		
		self.result=Gtk.Label('')
		
		self.result_frame=Gtk.Frame(label='')
		self.type_frame=Gtk.Frame(label='Type')
		
		self.type_url=Gtk.RadioButton(group=None,label='URL')
		self.type_file=Gtk.RadioButton(group=self.type_url,label='File')
		
		
		self.predict_button=Gtk.Button(label='Predict Category')
		self.predict_button.connect('clicked',self.predict_category)
		
		
		self.browse_button=Gtk.Button(label='browse')
		self.browse_button.connect('clicked',self.browse_file)
		
		self.file_chooser=Gtk.FileChooserDialog(title=None, parent=None, action=Gtk.FileChooserAction.OPEN, buttons=("Select",Gtk.ResponseType.OK,"Cancel",Gtk.ResponseType.CANCEL))
		
		self.box1.pack_start(self.box2,False,False,0)
		self.box2.pack_start(self.label1,False,False,0)
		self.box2.pack_start(self.input,True,True,0)
		self.box2.pack_start(self.browse_button,False,False,0)
		self.box1.pack_start(self.type_frame,False,False,0)
		self.type_frame.add(self.box3)
		self.box3.pack_start(self.type_url,True,True,0)
		self.box3.pack_start(self.type_file,True,True,0)
		self.box1.pack_start(self.predict_button,False,False,0)
		self.box1.pack_start(self.result_frame,True,True,0)
		self.result_frame.add(self.result)
		#self.box1.pack_start(self.result,True,True,0)
		
		
	def browse_file(self,widget):
		if self.file_chooser.run()==Gtk.ResponseType.OK:
			result=self.file_chooser.get_filename()
			self.input.set_text(result)
		self.file_chooser.hide()
		
	def predict_category(self,widget):
		
		if self.input.get_text()=='':
			self.result_frame.set_label('Error')
			self.result.set_markup("<span font='20' color='red'>No input</span>")
			return
		if self.type_url.get_active()==True:
			try:
				obj=WebPage(self.input.get_text())
				text=obj.getPureText()
			
				words=seperateWords(text)
				words=convertToLower(words)
				words=removeStopWords(words)
				words=applyStemming(words)
				freq=genFreqDict(words)
				freq=removeAnom(freq)
				category=naive_bayes(freq)
				self.result_frame.set_label('Category')
				self.result.set_markup("<span font='20' color='black'>"+category+"</span>")
			except ValueError:
				self.result_frame.set_label('Error')
				self.result.set_markup("<span font='20' color='red'>URL/PARSE Error:Unable to retrieve content</span>")
			except HTTPError:
				self.result_frame.set_label('Error')
				self.result.set_markup("<span font='20' color='red'>Unable to connect</span>")
			
			
		else:
			try:
				obj=HtmlFile(self.input.get_text())
				text=obj.getPureText()
				words=seperateWords(text)
				words=convertToLower(words)
				words=removeStopWords(words)
				words=applyStemming(words)
				freq=genFreqDict(words)
				freq=removeAnom(freq)
				category=naive_bayes(freq)
				self.result_frame.set_label('Category')
				self.result.set_markup("<span font='20' color='black'>"+category+"</span>")
			except FileNotFoundError:
				self.result_frame.set_label('Error')
				self.result.set_markup("<span font='20' color='red'>File Not Found</span>")
			
		
		
win=myWindow()
win.connect('delete-event',Gtk.main_quit)
win.set_title("Webpage category predictor")
win.set_size_request(600,300)
win.set_resizable(False)
win.show_all()
Gtk.main()
