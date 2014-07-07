TWISTER SETUP!!

The Twister Pipeline is used to process genomic sequence information on a computer cluster.

There are a lot of steps... I probably did not get all of them down, but here are the key components.


- Obtain a linux machine or computer cluster. 

- Follow steps on http://www.iterativemapreduce.org/userguide.html
	- Do not use NaradaBrokering
	- Use ActiveMQ broker instead (likely have to install)
	- Any steps involving NaradaBrokering, skip or do with AMQ.

	-**IP address needs to be changed in appropriate files every time this is run from new nodes/computer: 
		TWISTER/bin/nodes
		
		url in amq.properties in TWISTER/bin

	-*Make sure other file locations are correct in files mentioned in the userguide above

- Download ANT from Apache - Used to compile .jar files (JAVA)
	- Move activemq.....jar file to twister-0.9/lib/

- Set up environmental variables in .bashrc so that you don't have to do it every single session.
	- TWISTER_HOME
	- ANT_HOME
	- JAVA_HOME
	- AMQ_HOME (check .bashrc file to see if environmental variable is AMQ_HOME or ACTIVEMQ_HOME if it already exists)

- Optional: Download JAVA JDK in order to have original JDK as a backup.

1. Start ActiveMQ: AMQ_HOME/bin/activemq console
2. Run start_twister.sh from TWISTER_HOME/bin


NOTES:
	-ActiveMQ Broker is only run on one node, or on a seperate machine in cases of huge data sets.


------RUNNING Smith-Waterman------------------------------------------------------------------------

- In twister directory, go to samples/dacidr/
- pwaFileSpliter.sh function splits sequence file into smaller partitions (easier to process)
- pwaMul.sh function performs distance matrix calculations
- resulting files are in directory specified when prior functions are run.


	[lsaggu@i97 dacidr]$ ./pwaFileSpliter.sh
	args:  [gene_seq_file] [sequence_count] [num_of_partitions] [out_dir] [gene_block_prefix] [output_idx file] [Alphabet]
	[lsaggu@i97 dacidr]$ ./pwaFileSpliter.sh ~/data/test/4640_fasta.txt 4640 16 ~/data/test/16/ input_ ~/data/test/4640_16.idx RNA
		
		num_of_partitions = number of cores (nodes*cores) Don't include head node  Partitions gene sequence files into more manageable sized units
		
		out_dir = directory to output files
		
		gene_block_prefix = prefix before file name (i.e. input_???)
		
		output_idx file = location/name of file to store output idx....
		
		Alphabet = alphabet to use to read sequences: 'RNA' in most cases.
		


	[lsaggu@i97 dacidr]$ ./pwaMul.sh
	THis generates pid_ as well
	args:  [num_of_map_tasks] [num_of_reduce_tasks] [sequence_count] [num_of_partitions] [data_dir] [gene_block_prefix] [tmp_output_prefix] 		[output_map_file] [aligner type][score matrix type] [sequence type]
	[lsaggu@i97 dacidr]$ ./pwaMul.sh 16 4 4640 16 ~/data/test/16/ input_ swg_ 123 SWG edn RNA
	
		num_of_map_tasks = number of cores (nodes*ppn) Don't include head node
		
		num_of_reduce_tasks = number of nodes (Don't include head node)
		
		sequence_count = number of sequences
		
		num_of_partitions = number of cores
		
		data_dir = directory in which data was stored (same as out_dir from pwaFileSplitter)
		
		gene_block_prefix = prefix before file name (same as from pwaFileSplitter)
		
		tmp_output_prefix = prefix for output files
		
		aligner type = SWG or NW
		
		score matrix type = edn or blo
		
		sequence type = RNA or DNA



------RUNNING MDS-----------------------------------------------------------------------------------
FIRST RUN RANDOM WEIGHTS
- Generate a random weights output folder.
- In Twister_HOME directory, go to samples/dacidr
- Weights indicate significance of certain data points

	randomWeights.sh [1. output weighted matrix] [2. row] [3. col] [4. percentage] [5. symmetric (0:no; 1:yes)] [6. weight value]

- 1. where output weight matrix directory will be.
- 2. number of sequences
- 3. number of sequences
- 4. percentage of points to be given weight of 0 (typically 0)
- 5. 0
- 6. 1


NEXT, SPLIT WEIGHTS
- In TWISTER_HOME/samples/dacidr
- This splits the weight matrix file

	mdsFileSplit.sh [1. Data File ] [2. Temporary directory to split data ] [3. Temp file prefix ] [4. Output IDs file ] [5. Num map tasks ]
			[6. row size ] [7. column size] [8. Type of input value format (0: short; 1: double)]

1. output weight file from randomweights.sh
2. directory to store split data (will be same as input directory for MDS)
3. given by user: can be anything (weights_all1_)
4. output idx file: same as pwaFileSpliter
5. number of cores (ppn * nodes)
6. number of sequences
7. number of sequences
8. weight and distance matrices are in short (0)


- In Twister directory, go to samples/dacidr/
- mds scales data points.
- resulting files are in a specified directory.

	run_dasmacof_cg_mem.sh [1. Num map tasks ] [2. Input Folder] [3. Input File Prefix] [4. Input Weight Prefix] [5. IDs File ] 
				[6. Label Data File ] [7. Output File ] [8. Threshold value ] [9. The Target Dimension ] 
				[10. Cooling parameter (alpha) ] [11. Input Data Size] [12. Final Weight Prefix] [13. CG iteration num] 
				[14. CG Error Threshold]

- 1. The number of cores running job (nodes * ppn)
- 2. Output folder of pwaMul.sh (Distance files)
- 3. <Output prefix from pwaMul>_pid_
- 4. same as temp file prefix from mdsFileSplit
- 5. same as output IDs file from mdsFileSplit
- 6. "NoLabel"
- 7. Where output will go.
- 8. 0.000001 (resolution)
- 9. 3 (3D)
- 10. 0.95
- 11. number of sequences
- 12. Same as 4
- 13. 20
- 14. 1 



