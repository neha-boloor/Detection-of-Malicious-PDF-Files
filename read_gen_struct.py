from re import *
import pprint
from pprint import pprint
import csv

file_type = ""
p = "./peepdf_0.3/peepdf.py"
mypath = ""
f = ""

class PDF:
	def __init__(self,name,size,indirect_objs,versions,streams,cmp_objs,obj_streams,xref_streams,js_objs):
		self.name = name
		self.size = size
		self.indirect_objs = indirect_objs
		self.versions = versions
		self.streams = streams
		self.cmp_objs = cmp_objs
		self.obj_streams = obj_streams
		self.xref_streams = xref_streams
		self.js_objs = js_objs

	def print_attributes(self):
		print self.name
		print self.size
		print self.indirect_objs
		print self.versions
		print self.streams
		print self.cmp_objs
		print self.obj_streams
		print self.xref_streams
		print self.js_objs

	def get_list(self):
		temp = [self.name,self.size,self.indirect_objs,self.versions,self.streams,self.cmp_objs,self.obj_streams,self.js_objs]
		return temp


def read_file(ftype):
	global file_type,mypath,f,p
	if ftype:
		file_type = "malicious"
		fname = "gen_struct_malicious.txt"
	else:
		file_type = "clean"
		fname = "gen_struct_clean.txt"

	f = open(fname,'r')
	temp = ""
	pdfs = []
	for line in f.readlines():
		if line.strip() == "#":
			pdfs.append(temp)
			temp = ""
		else:
			temp = temp + line.strip()
			temp = temp + '\n'
	f.close()
	print "%d PDF files were scanned" %(len(pdfs))

	if ftype:
		fname = "gen_struct_malicious.csv"
	else:
		fname = "gen_struct_clean.csv"

	file = open(fname,"a")

	file.write('Filename,Size,Indirect Objects,Versions,Streams,Compressed Objects,Object Streams,JavaScript Objects'+'\n')
	wr = csv.writer(file, quoting = csv.QUOTE_ALL)

	patterns = ["File:.*","Size:.*","Objects:.*","Version\s.*","Streams:.*","Compressed objects\s.*","Object streams\s.*","Xref streams\s.*","Objects with JS code\s.*"]
	labels = ["name","size","indirect_objs","versions","streams","cmp_objs","obj_streams","xref_streams","js_objs"]
	pdf_obj = []

	for i in pdfs:
		temp = dict()
		name =  search(patterns[0],i)
		cmp_obj = 0
		obj_stream = 0
		xref_stream = 0
		js_obj = 0
		if(name):
			name = name.group(0).split(' ')[1]
		size =  search(patterns[1],i)
		if(size):
			size = size.group(0).split(' ')[1]
		indirect =  search(patterns[2],i)
		if(indirect):
			indirect = indirect.group(0).split(' ')[1]
		versions = len(findall(patterns[3],i))
		streams =  search(patterns[4],i)
		if(streams):
			streams = streams.group(0).split(' ')[1]
		temp_cmp_obj =  search(patterns[5],i)
		if(temp_cmp_obj):
			temp_cmp_obj = temp_cmp_obj.group(0).split(' ')[2]
			cmp_obj = search("\d+",temp_cmp_obj).group(0)
		temp_obj_stream =  search(patterns[6],i)
		if(temp_obj_stream):
			temp_obj_stream = temp_obj_stream.group(0).split(' ')[2]
			obj_stream = search("\d+",temp_obj_stream).group(0)
		temp_xref_stream =  search(patterns[7],i)
		if(temp_xref_stream):
			temp_xref_stream = temp_xref_stream.group(0).split(' ')[2]
			xref_stream = search("\d+",temp_xref_stream).group(0)
		temp_js_obj =  search(patterns[8],i)
		if(temp_js_obj):
			temp_js_obj = temp_js_obj.group(0).split(' ')[4]
			js_obj = search("\d+",temp_js_obj).group(0)

		'''
		print name
		print size
		print indirect
		print versions
		print streams
		print cmp_obj
		print obj_stream
		print xref_stream
		print js_obj '''

		temp = PDF(name,size,indirect,versions,streams,cmp_obj,obj_stream,xref_stream,js_obj)
		wr.writerow(temp.get_list())
		pdf_obj.append(temp)


# read_file(1)

