from os import listdir
from os.path import isfile, join
import subprocess
import os
import sys

mypath = "/home/neha/Projects/IAS/CLEAN_PDF_9000_files/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

f = "/home/neha/Projects/IAS/CLEAN_PDF_9000_files/"
p = "/home/neha/Projects/IAS/peepdf_0.3/peepdf.py"
file = open("tree-gen-output-clean.txt","a")

count = 1
for i in onlyfiles:
	print count
	count += 1
	#output = subprocess.check_output(["python",p,"-f",f])	
	output = subprocess.Popen(["python",p,"-fs","command_file.txt",f+i],stdout=subprocess.PIPE).communicate()[0]
	file.write(str("File: "+i))
	file.write(output)
	file.write("#\n\n")

file.close()