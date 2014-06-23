import sh
from sh import ssh
from sh import scp

#Test connection
#result = ssh("india.futuregrid.org", "pwd") #Runs one command at a time
#print result
#print "Success"

class PBS:
	"""Generates and submits scripts to be run in cluster"""

	def __init__(self, host):
		self.host = host

	def generate_script(self, scriptPath, nodes, ppn, time, email, jname, qname):
    		#Currently only creates Twister script which performs SWG and PWC
	    script = """#PBS -k o
#PBS -l nodes=%s:ppn=%s, walltime=%s
#PBS -M %s
#PBS -m abe
#PBS -N %s
#PBS -j oe
#PBS -q %s
#
#

set_nodes()
{
    > $TWISTER_HOME/bin/nodes #empties nodes file
    
    l=0
    while read line
    do
    let x=$l%%%s
    if (($x == 0))
    then
        echo $line >> $TWISTER_HOME/bin/nodes
    fi
    ((l++))
    done < $PBS_NODEFILE
	
    sed -i \"1d\" $TWISTER_HOME/bin/nodes
}
	
set_amq()
{
    read firstline < $PBS_NODEFILE
    sed -i \"53c\uri = failover:(tcp://$firstline:6161)\" $TWISTER_HOME/bin/amq.properties
}
set_nodes
set_amq

cp $TWISTER_HOME/bin/twister.properties

$AMQ_HOME/bin/activemq console &> ~/amq.out &
$TWISTER_HOME/bin/start_twister.sh &> ~/twister.out &

sleep 10

# NOW, RUN FUNCTIONS TO PROCESS DATA!

""" %(nodes, ppn, time, email, jname, qname, ppn)
        
	    #WRITE SCRIPT TO FILE - This file will be transferred with submit method
	    scriptfile = open(scriptPath, "w")
	    scriptfile.write(script)
	    scriptfile.close()

	def submit(self, script, label=None):
		"""Submits and runs a given script with given parameters on cluster"""
		
		#transfer script file to remote host
		scpHost = self.host + ":~"
		scp(script, scpHost)

		result = ssh(self.host, "qsub", script)
		#Return an id...
		return result

	def get_status(self, jobid):
		result = ssh(self.host, "checkjob", jobid)
		return result

	def transfer(self, files):
				

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
		clusterLink.py <host> <scriptPath> (-s | -t <nodes> <ppn> <time> <email> <jname> <qname>)
		clusterLink.py <host> -u <jobid>
		clusterLink.py <host> -f <files>
	
	Options:
		-h --help		Displays this help message
		-p <sciptPath>		path of script (existing or to be created)
		-s <host>		Submit given script to given host
		-t <parameters>		Creates script with given parameters
		-u <jobid>		Return the status of the given job
		-f <files>		transfers files at address or directory to host

		-p -t			Generates script and saves it at given scriptPath
		-p -s			Submits script at given scriptPath to given host
		-p -s -t		Generates and saves script at given scriptPath and submits script to host
	"""
	
	arguments = docopt(docString, version="cyberLink 1.0")

	pbs = PBS(arguments["<host>"])

	if arguments["-t"]:
		print "Started"
		nodes = arguments["<nodes>"]
		ppn = arguments["<ppn>"]
		time = arguments["<time>"]
		email = arguments["<email>"]
		jname = arguments["<jname>"]
		qname = arguments["<qname>"]
		pbs.generate_script(arguments["<scriptPath>"], nodes, ppn, time, email, jname, qname)
		
	if arguments["-s"] and arguments["-t"]:
		jobid = pbs.submit(arguments["<scriptPath>"])
		print "Job ID: " + jobid

	elif arguments["-s"]:
		print "Started"
		pbs.submit()

	if arguments["-u"]:
		print pbs.get_status(arguments["<jobid>"])

	if arguments["-f"]:
		pbs.transfer(arguments["<files>"])

	print "Complete"
