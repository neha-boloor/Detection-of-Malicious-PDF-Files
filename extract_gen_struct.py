from os import listdir
from os.path import isfile, join
import subprocess
import os
import sys
import threading


file_type = ""
p = "./peepdf_0.3/peepdf.py"
mypath = ""
f = ""
count =0

#running the PeePDF command 
class RunCmd(threading.Thread):
	def __init__(self, cmd, timeout,file_type):
		threading.Thread.__init__(self)
		self.cmd = cmd
		self.timeout = timeout
		self.fname = "./gen_struct_"+str(file_type)+".txt"
		self.file = open(self.fname,"a")

	def run(self):
		self.p = subprocess.Popen(self.cmd,stdout=subprocess.PIPE)
		self.p.wait()
		print "Sucessful",count
		output = self.p.communicate()[0]
		self.file.write(output)
		self.file.write("#\n\n")

	def Run(self):
		self.start()
		self.join(self.timeout)
		if self.is_alive():
			print "Terminated",count
			self.p.terminate()      
			self.join()

def extract(ftype):
	global count 
	global file_type,mypath,f,p
	if ftype:
		file_type = "malicious"
	else:
		file_type = "clean"

	if ftype == 1:
		mypath = "./MALWARE_PDF_PRE_04-2011_10982_files/"
		f = "./MALWARE_PDF_PRE_04-2011_10982_files/"
	elif ftype == 2:
		mypath = "./CLEAN_PDF_9000_files/"
		f = "./CLEAN_PDF_9000_files/"
	else:
		mypath = "./TEST"
		f = "./TEST"

	onlyfiles = [fname for fname in listdir(mypath) if isfile(join(mypath, fname))]

	for i in onlyfiles:
		count += 1
		RunCmd(["python",p,"-f",f+i], 60,file_type).Run()

extract(1)