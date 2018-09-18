from os import listdir
from os.path import isfile, join
import subprocess
import os
import sys
import threading
import time
from datetime import datetime
from threading import Thread

file_type = ""
p = "./peepdf_0.3/peepdf.py"
mypath = ""
f = ""

#running the PeePDF command 
class RunCmd(threading.Thread):
    def __init__(self, cmd, timeout,thread_id,file_type):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout
        self.thread_id = thread_id
        self.fname = "./ParallelOutput/output_"+str(file_type)+str(thread_id)+".txt"
        self.file = open(self.fname,"a")

    def run(self):
        self.p = subprocess.Popen(self.cmd,stdout=subprocess.PIPE)
        self.p.wait()
        output = self.p.communicate()[0]
        if output!="":
            self.file.write(output)
            self.file.write("#\n\n")

    def Run(self):
        self.start()
        self.join(self.timeout)
        if self.is_alive():
        	self.p.terminate()      
        	self.join()


def thread_call(temp,thread_id,file_type):
    for i in temp:
    	RunCmd(["python",p,"-f",f+i], 60,thread_id,file_type).Run()

def extract(ftype):
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

    thread_load = len(onlyfiles)/10 
    print "Number of PDFs:",len(onlyfiles)
    print "Load per Thread:",thread_load
    start = datetime.now()
    flag = False
    threads = [] 

    for i in range(0,len(onlyfiles),thread_load):
        if ((len(onlyfiles) - (i)) < (3*thread_load/2)):
            temp = onlyfiles[i:]
            flag = True
            print "Thread:",i/thread_load,"will handle",len(temp), "PDFs."
        else:
            temp = onlyfiles[i:i+thread_load]
            print "Thread:",i/thread_load,"will handle",len(temp), "PDFs."
        t = Thread(target=thread_call, args=(temp,(i/thread_load)+1,file_type,))
        threads.append(t)
        t.start()
        if flag:
            break

    for i in threads:
        i.join()
    end = datetime.now()
    print "Time Taken",end-start
    combine(file_type)

def combine(file_type):
    file = open("gen_struct_"+str(file_type)+".txt","a")
    for i in range(1,11):
        with open("./ParallelOutput/output_"+str(file_type)+str(i)+".txt", 'r') as content_file:
            content = content_file.read()
            file.write(content)
    file.close()

extract(1)
