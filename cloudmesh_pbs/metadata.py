#This file contains structure for JSON objects stored within MongoDB 
#using MongoEngine
#This is imported by submit.py and used for a history trace
#Resources for MongoEngine and MongoDB:
#http://docs.mongoengine.org/en/latest/tutorial.html
#http://docs.mongodb.org/manual/tutorial/getting-started/

from mongoengine import *

connect('submissions') #'submissions' is name of MongoDB database


class Comment(EmbeddedDocument):
	content = StringField()
	name = StringField(max_length=120)



class User(Document):
	email = StringField(required=True, primary_key=True)

	meta = {'allow_inheritance':True}

class Job(Document):
	name = StringField(required=True, primary_key=True)
	author = ReferenceField(User)

	nodes = StringField(max_length=10)
	ppn = StringField(max_length=10)
	walltime = StringField(max_length=50)
	queuename = StringField(max_length=50)

	tags = ListField(StringField(max_length=30)) #Possible future use
	comments = ListField(EmbeddedDocumentField(Comment))

	meta = {'allow_inheritance':True}

