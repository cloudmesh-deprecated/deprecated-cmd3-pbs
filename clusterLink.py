import sh
from sh import ssh
from sh import scp

#Test connection
#result = ssh("india.futuregrid.org", "pwd") #Runs one command at a time
#print result
#print "Success"

class PBS:
	"""Generates and submits scripts to be run in cluster"""

	def __init__(self, host, scriptPath):
		self.host = host
		self.script = scriptPath

	def submit(self, script=None, parameters=None, label=None):
		"""Submits a given script with given parameters to cluster"""
		if script is None:
			script = self.script
		
		#transfer script file to remote host
		scpHost = self.host + ":~"
		scp(script, scpHost)

		result = ssh(self.host, "qsub", script)
		#Return an id...
		return result

	def delete(self, id):
		"""Delete a script? by its id"""

	def delete_by_label(self, label):
		"""Delete a script? by its label"""


if __name__ == "__main__":
	"""Docopts will be used here for command line functionality"""
	import docopt
	from docopt import docopt
	
	docString = """ Cluster Link.
	Connect to and submit scripts to FutureGrid computer clusters.

	Usage:
		clusterLink.py (-h | --help)
		clusterLink.py (-e | --echo) <arg>
		clusterLink.py (-s <host> <scriptPath>)

	Options:
		-h --help		Displays this help message
		-e <arg>, --echo <arg>	Echo input text
		-s <host> <scriptPath>	Submit given script to given host
	"""
	
	arguments = docopt(docString, version="cyberLink 1.0")

	if arguments["-s"]:
		print "Started"
		pbs = PBS(arguments["<host>"], arguments["<scriptPath>"])
		pbs.submit()

	print "Complete"
