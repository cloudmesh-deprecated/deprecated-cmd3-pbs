#string = """
#Usage: test.py (-h | --help)
#       test.py -s [<name>] [<age>]

#Options:
#	(-h | --help)  	Displays this help message
#	-s		Show arguments
#    """

#from docopt import docopt


from mongoengine import *
#import metadata

class User(Document):
	name = StringField(required=True, primary_key=True)
	age = IntField()
	submissions = IntField()


if __name__ == "__main__":
	connect('test2')

	for user in User.objects:
		print user.name

	if User.objects.with_id("Rowland"):	
		print "True"
	else:
		print "False"

	for thing in User.objects(name="Rowland"):
		print thing.name

