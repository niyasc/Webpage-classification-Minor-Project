#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import sys

def make_training_set(database):
	'''
		Get a list of  dictionaries corresponding to each document and store it in mongo db
	''' 
	try:
		client=MongoClient()
		db=client.train
		db.drop_collection('training_set')
		training_set=db.training_set
		training_set.insert(database)
		
	except :
		print("Something went wrong !!!")
		sys.exit(1)
	finally:
		if client:
			client.disconnect()
		
