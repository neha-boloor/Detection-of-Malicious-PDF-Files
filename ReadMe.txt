PAPER TITLE : A Structural and Content-based Approach for a Precise and Robust Detection of Malicious PDF Files

INSTALLATION
1.	PeePDF
	Extract the ZIP file. To run PeePDF, run the python file named peepdf.py. However, to use all its functionalities it's recommended the installation of some external packages.
	The packages and libraries needed to have a full installation of peepdf are the following:
	1.1	PyV8 (external): execution of Javascript code. Install using the following commands.
		$git clone https://github.com/buffer/pyv8.git
		$cd pyv8
		$python setup.py build
		$sudo python setup.py install
	1.2	pylibemu (external): Libemu Python wrapper to emulate the shellcode execution. Install using the following commands.
		$sudo pip install pylibemu

2. 	Origami
	Origami is a ruby based tool and requires ruby 2.2 or above.
		$sudo apt-get install ruby2.2

*********************************************************************************************************************************************************************************************
Features:

*General Structure (8)-
1. size.
2. no. of versions.
3. no. of indirect objects.
4. no. of streams.
5. no. of compressed objects.
6. no. of object streams.
7. no. of X-ref streams.
8. no. of objects containing JavaScript.

*Content-based (2)-
9. PeePDF
10. Origami

*Object Structure (20)-
Most Characteristic Keywords

Here, a threshold for frequency was selected using k-means Clustering, which was then used for feature selection.
 
Total no. of features selected=8+2+20=30

*********************************************************************************************************************************************************************************************

Function of each script/file in the project folder:

1. extract_gen_struct.py: Extracts general features of all the pdf files given as input to it, by internally calling peepdf.py 

2. read_gen_struct.py : Generates and writes to gen_struct_malicious.csv, gen_struct_clean.csv, which contain the required 8 general features namely,(name,size,indirect,versions,streams,cmp_obj,obj_stream,xref_stream,js_obj)for malicious and benign respectively, off the general features obtained from the ouput of extract_gen_struct.py

3. extract_tree_struct.py: Extracts tree features (Keywords) by running tree command of peePDF on the input pdf file inputs.

4. read_tree_output.py: Creates and writes to keywords_mal.csv (77) and keywords_clean.csv(326), the characteristic keywords found as output of extract_tree_struct.py, and the number of files containing them.
 This is then fed to    'Kmeans.py'    it helps us select the best set of features(keywords in our case). List of keywords, their frequency within each file, cluster no. is written to keywords-mal-cluster.csv and keywords-clean-cluster.csv. To get an overall idea about the frequency of keywords selected as features and the ones that are not.
Finally, the selected key words (9,17) i.e. 20 unique ones and their individual frequencies per file, are written to frequency_malicious.csv and frequency_clean.csv

5.peepdfcheck.py : Checks if PeePDF allows complete scanning of the input PDF file. Since it performs a non-forced scan, if it takes longer than say 60 seconds to scan an input file, it is regarded as not legit. Writes it to peepdf_clean.csv and peepdf_mal.csv

6.origamicheck.py : Similar to the above script, this scans using origami and writes output to origami_clean.csv and origami_malicious.csv


7.merge.py : Merges all the features extracted namely : name,size,indirect,versions,streams,cmp_obj,obj_stream,xref_stream,js_obj,20 keywords, peepdf, origami . A total of 30 features for each file and stores in Features_malicious.csv and Features_clean.csv
Features.csv has the entire set of files and their feature set values including both clean and malicious files.

 
Creating train and test sets:
8. create_test_train.py : Writes final features of 70% of malicious and 70% of benign files each to TRAIN.csv
and remaining 30% to TEST.csv

9. SVM.py: This is used to classify a fresh test pdf file, as benign or malicious based on the training done using SVM classifier.
Prints the accuray, mean squared arror and also the names of the missclassified files.







# Detection-of-Malicious-PDF-Files
