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

mypath = "/home/neha/Projects/IAS/CLEAN_PDF_9000_files/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

f = "/home/neha/Projects/IAS/CLEAN_PDF_9000_files/"
p = "/home/neha/Projects/IAS/peepdf_0.3/peepdf.py"
peepdf = dict()
file = open("peepdf-check-clean.csv","a")

class RunCmd(threading.Thread):
    def __init__(self, cmd, filename, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout
        self.filename = filename

    def run(self):
        self.p = subprocess.Popen(self.cmd,stdout=subprocess.PIPE)
        self.p.wait()
        output = self.p.communicate()[0]
        print count
        if(output==""):
            file.write(self.filename)
            file.write(",Yes"+'\n')
        else:
            file.write(self.filename)
            file.write(",No"+'\n')

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
    RunCmd(["python",p,f+i],i,60).Run()

file.close()