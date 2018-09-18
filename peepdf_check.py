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

def timeout( p ):
    if p.poll() is None:
        print 'Error: process taking too long to complete--terminating'
        p.kill()

class RunCmd(threading.Thread):
    def __init__(self, cmd, filename, timeout,file_type):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout
        self.filename = filename
        self.fname = "./peepdf_"+str(file_type)+".csv"
        self.file = open(self.fname,"a")

    def run(self):
        self.p = subprocess.Popen(self.cmd,stdout=subprocess.PIPE)
        self.p.wait()
        output = self.p.communicate()[0]
        print count
        if(output==""):
            self.file.write(self.filename)
            self.file.write(",Yes"+'\n')
        else:
            self.file.write(self.filename)
            self.file.write(",No"+'\n')

    def Run(self):
        self.start()
        self.join(self.timeout)
        if self.is_alive():
        	print "Terminated",count
        	self.p.terminate()      #use self.p.kill() if process needs a kill -9
        	self.join()


def extract(ftype):
    global count 
    global file_type,mypath,f,p
    if ftype:
        file_type = "malicious"
    else:
        file_type = "clean"

    if ftype:
        mypath = "./MALWARE_PDF_PRE_04-2011_10982_files/"
        f = "./MALWARE_PDF_PRE_04-2011_10982_files/"
    else:
        mypath = "./CLEAN_PDF_9000_files/"
        f = "./CLEAN_PDF_9000_files/"
        
    onlyfiles = [fname for fname in listdir(mypath) if isfile(join(mypath, fname))]

    for i in onlyfiles:
        count += 1
        RunCmd(["python",p,f+i],i,60,file_type).Run()

# extract(0)