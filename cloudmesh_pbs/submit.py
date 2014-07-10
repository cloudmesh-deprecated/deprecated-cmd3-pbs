#!/usr/bin/python2.7
import sh
from sh import ssh
from sh import scp

import docopt
from docopt import docopt

    
#Test connection
#result = ssh("india.futuregrid.org", "pwd") #Runs one command at a time
#print result
#print "Success"



def shell_command_pbs(arguments):
	"""Connect to and submit scripts to FutureGrid computer clusters.

	Usage:
		submit.py (-h | --help)
		submit.py <host> <scriptPath> -s 
	        submit.py <host> <scriptPath> [-s] [-t] -c <nodes> <ppn> <time> <email> <jobname> <queuename> <executablePath>
		submit.py <host> -u <jobid>
		submit.py <host> -f <filePath> [-r]
	
	Options:
		(-h --help)	 Displays this help message
		-s <host>	 Submit given PBS script to given host
		-c <parameters>	 Creates PBS script with given parameters and saves it to <scriptPath>
		[-t]		 Creates a TwisterPBS script instead of a PBS script
		
		-f <filePath>	 transfers file directory or file at address to host
		[-r]		 indicates that files are located on a remote machine

		-u <jobid>	 Return the status of the given jobid

        Examples:
		submit.py -h
        	submit.py -s -t india.futuregrid.org ./myPBSScript 2 8 24:00:00 me@myemail.com job queue
		submit.py -s india.futuregrid.org ./myPremadePBSScript
		submit.py -f india.futuregrid.org ./myfiles
    """

#	arguments = docopt(docString, version="cyberLink 1.0")

	if arguments["-t"]:
		pbs = TwisterPBS(arguments["<host>"])
	else:
		pbs = PBS(arguments["<host>"])

	if arguments["-c"]:
		print "Started"
		nodes = arguments["<nodes>"]
		ppn = arguments["<ppn>"]
		time = arguments["<time>"]
		email = arguments["<email>"]
		jobname = arguments["<jname>"]
		queuename = arguments["<qname>"]
		executablePath = arguments["<executablePath>"]
		script = pbs.generate_script(nodes, ppn, time, email, jobname, queuename, executablePath)
		pbs.save_script(script, arguments["<scriptPath>"])
		
	if arguments["-s"]:
		print "Started"
		jobid = pbs.submit(arguments["<scriptPath>"])
		print "Job ID: " + jobid

	if arguments["-u"]:
		print pbs.get_status(arguments["<jobid>"])

	if arguments["-f"] and arguments["-r"]:
		pbs.transfer(arguments["<filePath>"], remote=True)
	elif arguments["-f"]:
		pbs.transfer(arguments["<filePath>"], remote=False)

	print "Complete"
    	




class PBS:
	"""Generates and submits scripts to be run in cluster"""

	def __init__(self, host):
		self.host = host

	def submit(self, scriptPath):
		""".. function:: submit(scriptPath):

		      Submits and runs a given local script with given parameters on cluster
			
		      :param scriptPath: path of script on local machine"""
		
		#transfer script file to remote host
		scpHost = self.host + ":~"
		scp(scriptPath, scpHost)

		result = ssh(self.host, "qsub", script)
		#Return an id...
		return result

	def generate_script(self, nodes, ppn, time, email, jobname, queuename, executablePath=""):
		""".. function:: generate_script(nodes, ppn, time, email, jobname, queuename, executablePath)
		     
		      Generate a string representing a basic PBS script

	              :param nodes: number of nodes desired on cluster
	    	      :param ppn: number of processors per node
	    	      :param time: time required for job: 'hh:mm:ss'
	    	      :param email: email to send job progress info
	    	      :param jobname: name of job
	    	      :param queuename: name of queue on which to run job
		      :param executablePath: path of executable file on machine which job will run"""

		script = """#PBS -k o
#PBS -l nodes %(nodes)s:ppn=%(ppn)s, walltime=%(time)s
#PBS -M %(email)s
#PBS -m abe
#PBS -N %(jobname)s
#PBS -j oe
#PBS -q %(queuename)s
#
#

%(executablePath)s
""" % vars()
		return script
	
	def save_script(self, script, scriptPath):
		""".. function:: save_script(script, scriptPath)
		      
		      Save script to the local scriptPath given

		      :param script: string representing PBS script
		      :param scriptPath: local path to store script"""

		#WRITE SCRIPT TO FILE - This file will be transferred with submit method
		scriptfile = open(scriptPath, "w")
		scriptfile.write(script)
		scriptfile.close()

	def get_status(self, jobid):
		""".. function:: get_status(jobid)

		      Return the current status of the job referenced by the given jobid

		      :param jobid: id of job to check on host"""

		result = ssh(self.host, "checkjob", jobid)
		return result

	def transfer(self, filePath, remote=False):
		""".. function:: transfer(files, remote)

		      Transfer files, local or remote, to host specified on command line

		      :param filePath: path/address of files to be transferred to host
		      :param remote: boolean dictating if files are remote (true) or local (false)"""

		if remote:
			sh.wget("-N", "-P", "./files", filePath) #Places files within a local directory named "files"
			scpHost = self.host + ":~"
			scp("-r", "./files", scpHost)
		else:
			scpHost = self.host + ":~"
			scp(filePath, scpHost) #May need to edit command to recursively handle directories

	def delete(self, id):
		""".. function:: delete(id)

		      Delete a script?/job? by its id
		
		      :param id: id of job on cluster.."""

		return None

	def delete_by_label(self, label):
		""".. function:: delete_by_label(label)

		      Delete a script?/job? by its label

		      :param label: label of job on cluster.."""

		return None

class TwisterPBS(PBS):

	def generate_script(self, nodes, ppn, time, email, jobname, queuename, executablePath=""):
		""".. function:: generate_script(nodes, ppn, time, email, jobname, queuename, executablePath)

		      See PBS.generate_script(): Creates a twister specific PBS script string
			
		      :param nodes: nodes to use on cluster
		      :param ppn: processors to use per node
		      :param time: time required for job: 'hh:mm:ss'
		      :param email: email to send job progress info
		      :param jobname: name of job
		      :param queuename: name of queue on which to run job
		      :param executablePath: path of an executable to be run on host"""

		#Currently only creates Twister script which performs SWG and PWC
		twistscript = super.generate_script(nodes, ppn, time, email, jobname, queuename, executablePath) + """
set_nodes()
{
    > $TWISTER_HOME/bin/nodes
    
    l=0
    while read line
    do
    let x=$l%%%(ppn)s
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

""" % vars()

		return twistscript


def main():
    arguments = docopt(shell_command_pbs.__doc__)
    shell_command_pbs(arguments)

        
if __name__ == "__main__":
    main()
