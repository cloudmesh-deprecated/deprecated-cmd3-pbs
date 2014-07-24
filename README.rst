cloudmesh_pbs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python program which submits PBS jobs to computer clusters. This
program is titled submit.py (within cloudmesh_pbs)

Currently, the computer cluster in use is India on FutureGrid.


Further Project Information: 

	https://github.com/cloudmesh/reu/blob/master/doc/source/projects/bioinformatics.rst

Setting up submit.py within Cloudmesh environment
================================================
Make sure **Cloudmesh** and **CMD3** are installed.

::

  pip install -r requirements.txt

  python setup.py install

Running submit.py within Cloudmesh environment
================================================

::

  cm-pbs

  python cloudmesh_pbs/submit.py

  cm
  
**Within Cloudmesh Shell, the command to run submit.py is "pbs"**

Type "help pbs" in Cloudmesh Shell to view help text.

Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The goal of submit.py is to submit PBS scripts to computer clusters
  (currently on FutureGrid) and ultimately run these scripts on the
  cluster.

- Being able to transfer files to a computer cluster is also a goal of
  this program

- Connecting to computer clusters requires that local machine has ssh
  keys set up with FutureGrid

- A history trace has been implemented using MongoDB and MongoEngine
 The structure of objects within the database is found in metadata.py
 

**In order to transfer files to host, submit jobs, etc, you must have a working ssh connection! Editing submit.py methods may be necessary if password is required.**

**Enter host with user:password@host format on command line before editing code.**

See PBS.submit function in submit.py if encountering issues with a working ssh connection.

::

	Usage:
		submit.py (-h | --help)
		submit.py <host> <scriptPath> -s 
	        submit.py <host> <scriptPath> [-s] [-t] -c <nodes> 
                          <ppn> <time> <email> <jobname> <queuename>
		submit.py <host> -u <jobid>
		submit.py <host> -f <filePath> [-r]
	
	Options:
		(-h --help)	 Displays a help message
		-s <host>	 Submit given PBS script to given host
		-c <parameters>  Creates PBS script with given
                                 parameters and saves it 
                                 to <scriptPath>
		[-t]		 Creates a TwisterPBS script instead 
		                 of a PBS script
		-f <filePath>    Transfers file directory or file at 
                                 address to host
		[-r]		 indicates that files are located on 
                                 a remote machine
		-i <jobid>       Return the status of the given jobid
		-u <email>	 Retrun the history of the given user

        Examples:
		submit.py -h

        	submit.py -s -t india.futuregrid.org ./myPBSScript 2 8
		24:00:00 me@myemail.com job queue
			- creates and submits a PBS script with
                          requesting 2 nodes, 8 processors per node
                          for 24 hours. The email to send job info:
                          me@myemail.com. The job name is job and the
                          queue name is queue.

		submit.py -s india.futuregrid.org ./myPBSScript
			- submits the local script ./myPBSScript to
                          india.futuregrid.org

		submit.py -f india.futuregrid.org ./myfiles
			- transfers local file or directory ./myfiles
                          to india.futuregrid.org home directory

		submit.py -u me@myemail.com
			- returns history of user with given email

Scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- submit.py primarily functions to submit and run PBS scripts on computer clusters
- In the doc directory exist "example_script" and "twisterScript"

example_script
==================================================

Use this script as a basis for putting together your own script.

::

	#
	#
	#PBS -k o
	#PBS -l nodes=<numberOfNodes>:ppn=<numberOfProcessorsPerNode>,walltime=<hh:mm:ss>
	#PBS -M <email>
	#PBS -m abe
	#PBS -N <jobname>
	#PBS -j oe
	#PBS -q <queuename>
	#
	#

	echo "Started..."

	#Run any commands or Executables here
	
	<Command>
	<Executable>
	
	sleep 10
	
	echo "Done"

Parameters
_________________________________________________________
<numberOfNodes>: 			The number of nodes desired for the job

<numberOfProcessorsPerNode>: 		The number of processors per node desired (typically 8)

<hh:mm:ss>				The walltime or the time necessary for the job to run in hours:minutes:seconds

<email>:				The email to which job success/error information is sent

<jobname>:				Name of the job to be run

<queuename>:				Name of the queue on which to run this job

<Command>:				Command to be run by script (eg. echo "Blah blah blah")
				
<Executable>:				Executable file to be run by script. This file should be on the same machine that will run this script

Notes
______________________________________________________________
Any number of <Command> and/or <Executable arguments may be given

Usually, it is a good idea to run "sleep <x>" for x number of seconds between commands/executables

In order to run a command or executable in the background use "&":

::

	#Script Body
	
	Command1 arg1 arg2 arg3 &

	wait

	#Remainder of Script

"wait" is sometimes used to prevent script from "hanging" 
(see http://tldp.org/LDP/abs/html/x9644.html#WAITHANG)

A complete script may be submit and run on a remote host using submit.py's -s option


Check out these links which explain qsub options (-k, -l, etc):
____________________________________________________________________
- http://www.nas.nasa.gov/hecc/support/kb/Commonly-Used-QSUB-Options-in-PBS-Scripts-or-in-the-QSUB-Command-Line_175.html

- http://rcc.its.psu.edu/user_guides/system_utilities/pbs/

- **User guide to PBS:** http://scsb.utmb.edu/facilities/random/protocols/pbs-mit-user-guide.htm

twisterScript
==================================================
Regard twisterScript in doc directory

 - This script sets up the Twister and ActiveMQ environments as long as their classpaths are loaded on the machine this script is run on
 - set_nodes() sets the nodes appropriately for twister to run.
	- See http://scsb.utmb.edu/facilities/random/protocols/pbs-mit-user-guide.htm for info on PBS_NODEFILE
 - set_amq() sets the headnode in the amq.properties file in the $TWISTER_HOME/bin/ directory

After the nodes are set, the environment is started with lines 52 and 53

The Twister Pipeline executable functions are then exemplified in lines 61, 64, 69, 72, and 75

Each executable is seperated by a sleep command as suggested previously.

Usage
_________________________________________________
**Adjust arguments for executable functions as necessary depending on existing data and file structures**

**If only running specific executables, comment out others using '#' at the beginning of the line.**


Progress
==================================================
Look at doc/journal.rst

Future Work
==================================================
- Create a daemon to monitor existing jobs and return job progress

- This daemon would also return output once jobs are completed

- Integrate this tool into Cloudmesh GUI
