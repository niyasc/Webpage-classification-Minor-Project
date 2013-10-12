#!/usr/bin/python3

from gi.repository import Gtk

class myWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self,title='Hello, World')
		
		self.box1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		self.box2=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		self.box3=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		self.add(self.box1)
		
		self.label1=Gtk.Label('File/URL')
		
		self.input=Gtk.Entry()
		
		self.result=Gtk.Label('Enter a url or select file to predict category')
		
		self.result_frame=Gtk.Frame(label='Category')
		self.type_frame=Gtk.Frame(label='Type')
		
		self.type_file=Gtk.RadioButton(group=None,label='File')
		self.type_url=Gtk.RadioButton(group=self.type_file,label='URL')
		
		self.predict_button=Gtk.Button(label='Predict')
		
		
		self.browse_button=Gtk.Button(label='browse')
		self.browse_button.connect('clicked',self.browse_file)
		
		self.file_chooser=Gtk.FileChooserDialog(title=None, parent=None, action=Gtk.FileChooserAction.OPEN, buttons=("Select",Gtk.ResponseType.OK,"Cancel",Gtk.ResponseType.CANCEL))
		
		self.box1.pack_start(self.box2,False,False,0)
		self.box2.pack_start(self.label1,False,False,0)
		self.box2.pack_start(self.input,True,True,0)
		self.box2.pack_start(self.browse_button,False,False,0)
		self.box1.pack_start(self.type_frame,False,False,0)
		self.type_frame.add(self.box3)
		self.box3.pack_start(self.type_file,True,True,0)
		self.box3.pack_start(self.type_url,True,True,0)
		self.box1.pack_start(self.predict_button,False,False,0)
		self.box1.pack_start(self.result_frame,True,True,0)
		self.result_frame.add(self.result)
		#self.box1.pack_start(self.result,True,True,0)
		
		
	def browse_file(self,widget):
		if self.file_chooser.run()==Gtk.ResponseType.OK:
			result=self.file_chooser.get_filename()
			self.input.set_text(result)
		self.file_chooser.hide()
		
		
win=myWindow()
win.connect('delete-event',Gtk.main_quit)
win.set_title("Webpage category predictor")
win.set_size_request(600,300)
win.set_resizable(False)
win.show_all()
Gtk.main()
