from os import listdir
from os.path import isfile, join
import subprocess
import os
import sys
import threading

def timeout( p ):
    if p.poll() is None:
        print 'Error: process taking too long to complete--terminating'
        p.kill()

mypath = "/home/neha/Projects/IAS/MALWARE_PDF_PRE_04-2011_10982_files/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

f = "/home/neha/Projects/IAS/MALWARE_PDF_PRE_04-2011_10982_files/"
p = "/home/neha/Projects/IAS/peepdf_0.3/peepdf.py"
file = open("gen-output-mal-parallel.txt","a")

'''
f2 = "61a1b7ceca9c96fc0ad4605600723e38bd9e27e4"
f1 = "00060c6f8c34a29e9aa4b87e1f00f87b38389a27"
temp=[]
temp.append(f2)
temp.append(f1)



for i in onlyfiles:
#for i in temp:
	#print f+i
	#output = subprocess.check_output(["python",p,"-f",f])	
	process = subprocess.Popen(["python",p,"-f",f+i],stdout=subprocess.PIPE)
	t = threading.Timer( 3.0, timeout, [process] )
	t.start()
	t.join()
	output = process.communicate()[0]
	file.write(output)
	file.write("#\n\n")
file.close()
'''

class RunCmd(threading.Thread):
    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout

    def run(self):
        self.p = subprocess.Popen(self.cmd,stdout=subprocess.PIPE)
        self.p.wait()
        print "Sucessful",count
        output = self.p.communicate()[0]
        file.write(output)
        file.write("#\n\n")

    def Run(self):
        self.start()
        self.join(self.timeout)
        if self.is_alive():
        	print "Terminated",count
        	self.p.terminate()      #use self.p.kill() if process needs a kill -9
        	self.join()

count = 0
for i in onlyfiles:
	count += 1
	RunCmd(["python",p,"-f",f+i], 60).Run()
file.close()