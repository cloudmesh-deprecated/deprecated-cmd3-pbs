cloudmesh_pbs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python program which submits PBS jobs to computer clusters. This
program is titled submit.py (within cloudmesh_pbs)

Currently, the computer cluster in use is India on FutureGrid.


Further Project Information: 

	https://github.com/cloudmesh/reu/blob/master/doc/source/projects/bioinformatics.rst

Setting up submit.py within environment
================================================

::

  pip install -r requirements.txt

  python setup.py install

Running submit.py within environment
================================================

::

  cm-pbs

  python cloudmesh_pbs/submit.py

  cm

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
 

-** In order to transfer files to host, submit jobs, etc, you must
 have a working ssh connection! Editing submit.py methods may be
 necessary if password is required or enter host with
 user:password@host format.


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
		-u <jobid>       Return the status of the given jobid

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

		submit.py -i me@myemail.com
			- returns history of user with given email


Progress
==================================================
Look at doc/journal.rst

Future Work
==================================================
- Create a daemon to monitor existing jobs and return job progress

- This daemon would also return output once jobs are completed

- Integrate this tool into Cloudmesh GUI
