#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle
import sys

def make_training_set(database):
	'''
		Get a list of  dictionaries corresponding to each document and store it in mongo db
	''' 
	try:
		pickle.dump(database,open('database.db','wb'))
		
	except :
		print("Something went wrong !!!")
		sys.exit(1)
		
