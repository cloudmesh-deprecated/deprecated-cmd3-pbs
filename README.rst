pip install -r requirements.txt
python setup.py install

cm-pbs
python cloudmesh_pbs/submit.py
cm

clusterLink
===========

Python program which submits PBS jobs to computer clusters.

Currently, the computer cluster in use is India on FutureGrid.


Progress

	6/23: 
	clusterLink.py successfully connects to cluster and submits a local scriptfile to be run.
	Currently working on developing generate_script method in order to dynamically create scripts.

	6/30:
	clusterLink.py renamed to submit.py - still working on reformatting string style for script creation


