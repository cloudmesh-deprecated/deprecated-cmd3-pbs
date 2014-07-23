IU-SROC 2014 Journal
BioInformatics Project under Dr. Geoffrey Fox, Saliya Ekenyake, Yang Ruan

Week 1
____________________________________________________________________________________________________________________________________________
6/4 
	- Project defined: Develop 3D tree mapping of 143K genetic code sequences using (improving upon) developed methods (DACIDR). Ultimately 		produce an image that appropriately displays relationship of genetic sequences to one another.

6/5 
	- Download and install Visual Studio (VS), Tortoise SVN (file backup software), attempt to build Pairwise Clustering Program in VS.
	- PWC tool (MDS tryout) Documentation: http://grids.ucs.indiana.edu/ptliupages/publications/Sequence%20Clustering%20Tools_draft_2.pdf
	- PWC tool is running.
	- Begun setting up accounts for Twister in order to run Smith-Waterman Algorithms and create Distance Matrix!
	- Added to FutureGrid Account

6/6 
	- PWC tool finished running. I will submit output files to Box.
	- Discussed new project: Developing interface that communicates with user and computer clusters. Interface would be user friendly and 				would communicate necessary information to clusters in order to return output to user.***
	- Set up git project page.
	- Accessed FutureGrid Account, and synced PWC files to my machine.
	- New Project! Outline and email Saliya, Yang, Dr. Fox about new Project: Develop framework/web interface for deploying MDS job using 				Twister on IU clusters.

Week 2
____________________________________________________________________________________________________________________________________________
6/9 
	- Finish downloading and setting up Twister Iterative MapReduce. See file TwisterPipelineSetup.txt for outline of Twister setup.
	- Downloaded/Installed onto FutureGrid cluster: JAVA JDK, Apache ANT, Apache ActiveMQ Broker
	- Managed to get Twister running
	- Ran algorithm to create Distance Matrix

	TODO: Update java code in futureGrid, Familiarize self with arguments for running algorithms
	Tomorrow: Work on MDS and create visualization! Sit with Saliya to work on other project component (web interface)

	
	[lsaggu@i97 dacidr]$ ./pwaFileSpliter.sh
	args:  [gene_seq_file] [sequence_count] [num_of_partitions] [out_dir] [gene_block_prefix] [output_idx file] [Alphabet]
	[lsaggu@i97 dacidr]$ ./pwaFileSpliter.sh ~/data/test/4640_fasta.txt 4640 16 ~/data/test/16/ input_ ~/data/test/4640_16.idx RNA
		
		num_of_partitions = number of cores....?  Partitions gene sequence files into more manageable sized units
		out_dir = directory to output files
		gene_block_prefix = prefix before file name (i.e. input_???)
		output_idx file = location/name of file to store output idx....
		Alphabet = alphabet to use to read sequences: 'RNA' in most cases.
		


	**pwaMul.sh**
	THis generates pid_ as well
	args:  [num_of_map_tasks] [num_of_reduce_tasks] [sequence_count] [num_of_partitions] [data_dir] [gene_block_prefix] [tmp_output_prefix]	[output_map_file] [aligner type][score matrix type] [sequence type]

	[lsaggu@i97 dacidr]$ ./pwaMul.sh 16 4 4640 16 ~/data/test/16/ input_ swg_ 123 SWG edn RNA

		ASK ABOUT ARGUMENTS!!!

6/10 
	- Continued to familiarize myself with Smith-Waterman code: How to submit jobs, what to expect as output.
	- Experimented with accessing cluster, and using bash commands.
	- Updated code from Yang to include mds scripts
	- *Began working on portal framework. Working on back-end which will accept user input and submit jobs to clusters.
	- Working on building script and connecting via ssh to computer cluster (futureGrid specifically for this instance.)

6/11 
	- Continued work.
	- Worked on portal framework - need to have Saliya review progress.
	- NEED TO CONNECT VIA SSH TO CLUSTER - SETUP SSH-KEY
	- Finished MDS on FutureGrid and reviewed resulting 3D graph in plotviz.
	- Need to set up environment in Quarry in order to run Twister.

6/12 
	- Finished setting up Twister/AMQ environments in Quarry
	- Met with Saliya and Yang to review progress. Will need to work with Yang to develop PBS script in Java
	- Saliya said he would look at connecting via ssh using jsch in java.
	- Waiting on nodes from Quarry....
	- Continuing to develop protal framework! Goal: Access futuregrid, submit simple job.

6/13 
	- Spent time working on protal framework - basic desgin and functionality...still need to establish ssh connection.
	- Worked with Yang on writing PBS script that will be deployed by java portal. EDIT: Still need to work on PBS script (6/16)
	- Met with mentors to discuss progress and upcoming goals
	- Redefined project goals: design a simple, back-end, program in Python which will interface with Cloudmesh and submit PBS job scripts to 		FutureGrid and similar clusters. 

Week 3
______________________________________________________________________________________________________________________________________
6/16 
	- Set up python libraries (sh and docopts) as well as environment.
	- Began designing clusterLink.py: uses sh library to connect to grid via command line and submit a PBS script to be run on the cluster
	- Began working on a test PBS script to be submitted to cluster.
	- Need to successfully submit a script to FutureGrid and have it run.
	- qsub command not found using shh from sh?

6/17 
	- Edited .bashrc on india.futuregrid.org: set path to QSUB_HOME directory. This fixed "command not found" error. (http://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path)
	- NEED TO: Ask about Quarry nodes.
	- SCP resource: http://www.hypexr.org/linux_scp_help.php
	- PBS resources: http://www.cerm.unifi.it/static/CLUSTER/cluster.html, https://www.msi.umn.edu/resources/job-submission-and-scheduling-pbs-scripts
	- ssh resource: http://bobjunior.com/linux/ssh-and-python/
	- docopt resource: https://github.com/docopt/docopt

	- Successfully sent script to run on cluster!

	- NEXT: Create PBS script to run PWA (Smith Waterman) process on FutureGrid.
	- RUN MDS on QUARRY on 56k + 1k data

	
6/18 
	- Continued to work on PBS script
	- Scripting guide: http://www.tldp.org/LDP/abs/html/ops.html
	- http://www.linuxquestions.org/questions/programming-9/how-can-i-do-multithreading-in-shell-scripting-904135/
	- stackoverflow.com
	- Finished basic outline for setting up nodes file in TWISTER_HOME/bin
	- Need to write function to edit amq.properties file
	- Also work on parameterizing function so that these scripts can be dynamically created in Python!

6/19 
	- Working on PBS script
	- Completed file modification functions in Bash script (twisterScript)
	- Completed simple script to run Twister.
	- Began debugging with Yang
	- Goal: successfully run script remotely on FutureGrid.

6/20 
	- Developed python function to dynamically create Twister script which will run SWG and PWC algorithms on given data
	- Still have some development left to do on this program and on this script.
	- Yang has received my script and will spend time looking over it and looking over his code so that it will run smoothly.
	- NEXT WEEK - need to meet with Yang and go over script and over Quarry Jobs!!!!!

Week 4
________________________________________________________________________________________________________________________________________
6/23 
	- Continued working on clusterLink.py script and on developing dynamic PBS script creation
	- Met with Yang to go over twisterScript: adjusted environmental variables and script executed successfully!
	- Met with Saliya to go over clusterLink.py progress
	- Will work on file transfer method and status update method.
	- Plan to meet on Wednesday (6/25) to go over integration of clusterLink.py with Cloudmesh

6/24 
	- Finished get_status and transfer methods within clusterLink.py
	- Need to test transfer method within clusterLink.py to ensure that remote files will be transferred.
	- Plan to meet with Saliya, Fugang, and Yang to discuss next steps.
	- Also, may need to touch base with Quarry administration about the node request.

6/25 
	- Tested get_status and transfer methods
	- Can successfully transfer remote files to cluster.
	- Met with Yang, Saliya, and Fugang to discuss integration with Cloudmesh.
	- Need to install cloudmesh and CMD3 in order to "inject" my code into the framework.
	- Will be working with Saliya and Yang to improve script generation

Week 5
_________________________________________________________________________________________________________________________________________
6/30 
	- Attempted to install Cloudmesh onto Saliya's Linux-Box
	- Determined that Ubuntu needed to be upgraded: Decided to look into another machine for install
	- Will work tomorrow to set up new machine.
	- May spend time developing clusterLink.py dynamic script creation
	- Gregor gave suggestions on how to improve script and clusterLink.py....possibly rename to submit.py
	- added TwisterPBS class and improved syntax of variables within string

	- http://cloudmesh.futuregrid.org/cloudmesh/developer.html
	- http://forums.devshed.com/python-programming-11/python-variables-strings-29994.html
	- docs.python.org

7/1 
	- Obtained new machine
	- Installed Ubuntu 14.04 on machine
	- Set up git and cloned cloudmesh repository
	- Installed CloudMesh
		Initial user/user manual??
		Need to figure out .yaml files
	- Still need to install CMD3 before being able to integrate submit.py
	- Can ssh access computer from another machine.

7/2 
	- Managed to run CMD3 in terminal
	- Working on integrating submit.py with cmd3
	- Gregor helped integrate submit.py into cmd3
	- spent time refining, cleaning up, and documenting code
	- need to set up quarry jobs
	- also need to talk to Saliya about next steps for program

7/3 
	- Set up SSH access to india on futuregrid from Ubuntu machine: check .bashrc
	- Was briefed on poster -NEED TO START
	- Worked on submit.py generate_script() - added ability to run an executable
	- Began integrating Celery management system into submit.py system.
	- Manual for OpenPBS
		- http://bose.utmb.edu/Compu_Center/Cluster_users/PBS%20HOWTO/openpbs_manual.pdf
	- Examples
		- http://bose.utmb.edu/Compu_Center/Cluster_users/PBS%20HOWTO/PBS_HOW_TO.html

Week 6
________________________________________________________________________________________________________________________________________
7/7 
	- Worked on installing Django and Celery for Python
	- Spent time reading up on celery and its usage
	- Worked with Yang to process test data
	- Began processing new data set

7/8 
	- Focused time working on poster
	- Continued processing new data
	- Need to talk to Fugang about Cloudmesh Usage... Submit doesn't work in cm shell
	- Need to request more Quarry nodes.

7/9 
	- Met with Saliya to discuss next steps
	- Need to process 57K sequences once nodes are obtained on Quarry
	- Need to set up MongoDB and MongoEngine - Develop history trace.
	- Need to Adjust AMQ memory
	- Need to meet with Fugang and discuss Cloudmesh integration
	- Worked on completing poster text - submitted it to be reviewed by Saliya and co.

7/10 
	- Continued developing poster text - placed it into ACM format
	- Installed MongoDB and MongoEngine
	- Began developing metadata.py file containing MongoDB document structure
	- Need to read up on MongoDB commands - retrieving documents.
7/11
	- Continued working on history trace with MongoDB
	- Began improving code: studying docopts and Mongo: how to edit existing docs within database
	- Researched ActiveMQ and memory management
	- Need to finish Mongo work in submit.py!!!!!

Week 7
_________________________________________________________________________________________________________________________________________
7/14
	- Adjusted configuration files for ActiveMQ
	- Continued processing 57K sequences
	- Continued working on developing history trace with Mongo
		- Completed definition and storage of users/jobs
		- Need to def function to query database and obtain history
			- get_jobs(user) function
			- get_job(jobname) function
			- get_user(email) function
			
7/15
	- Continued working on poster: Need to refine text and place graphics
		- Met with Khaliq and Saliya to obtain information
		- Submitted for further review
	- Tried to process 57K sequences: continued running into memory errors!
		- Adjusted memory requirements in config files - will try again.

7/16
	- Presented progress at IUPUI to fellow researchers
	- Attempted to run 57K sequences once more without any avail
	
7/17
	- Managed to begin processing 57K sequences with help of Yang
	- Began working on Career Portfolio assignment (for Seminar)
	- Further altered poster - DUE Tuesday

7/18
	- Continued to process 57K data
	- Worked on submit.py history trace and MongoDB access
	- Edited poster and submitted for review by mentors
	- Worked on Documentation of project.
	
Week 8
_______________________________________________________________________________________________________________________________________
7/21
	- Completed Paper and Poster -uploaded to Cloudmesh/REU repository
	- Attempted to finish processing 57K sequences
	- Documented progress on submit.py	

7/22
	- Began MDS on 57K sequences!
	- Successfully ran MDS on 57K sequences!!!
	- Finished and submitted poster
	- Documented progress
	- Worked on example_script and twisterScript documentation
	- Need to edit twisterScript
	- Need to finish documentation
	- Need to meet with Fugang about cloudmesh shell

7/23
	- Continued documentation of project
		- Defined example_script and twisterScript
	- Spoke to Fugang about Cloudmesh
		- The submit.py function is "pbs" in the Cloudmesh shell
		- The function appears to work
	- Need to meet with Saliya to discuss wrap up.


	
