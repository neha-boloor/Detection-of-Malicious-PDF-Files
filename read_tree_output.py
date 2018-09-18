import re
from pprint import pprint
import csv
import collections


file_type = ""
p = "./peepdf_0.3/peepdf.py"
mypath = ""
f = ""

def list_of_pdfs(filename):
	f = open(filename)
	temp = ""
	pdfs = []
	for line in f.readlines():
		if "#" in line.strip():
			pdfs.append(temp)
			temp = ""
		else:
			temp = temp + line.strip()
			temp = temp + '\n'
	print "%d PDF files were scanned." %(len(pdfs))
	return pdfs

def get_keyword_set(pdfs):
	keywords = set()
	for i in pdfs:
		_keywords = re.findall("/[a-zA-Z]+",i)
		_keywords = set(_keywords)
		keywords.update(_keywords)

	print len(keywords), "keywords found."
	return keywords

def get_frequency_keywords(keywords,pdfs):
	ni = dict()
	for i in keywords:
		ni[i] = 0
		for j in pdfs:
			temp = re.search(i,j)
			if temp:
				ni[i] = ni[i] + 1
	return ni

def print_to_csv(filename,ni):
	with open(filename, 'w') as outfile:
		outfile.write("Frequency")
		outfile.write(",Keyword")
		outfile.write("\n")
		for k,v in ni.items():
			outfile.write(str(v))
			outfile.write(","+str(k))
			outfile.write("\n")

def read_csv(filename):
	dataset = list()
	file = open(filename,'r')
	csv_reader = csv.reader(file)
	for row in csv_reader:
		if row[-1] == "cluster1":
			dataset.append(row[1])
	return dataset

def get_frequency_each_pdf(keywords,pdfs):
	freq_each_pdf = []
	for i in pdfs:
		freq = collections.OrderedDict()
		for j in keywords:
			if j=="File.*":
				fname = (re.search(j,i)).group(0).split(' ')[1]
				freq["Filename"] = fname
			else:
				freq[j] = len(re.findall(j,i))
		freq_each_pdf.append(freq)
	return freq_each_pdf

def read_output():
	pdfs_mal = list_of_pdfs("tree_struct_malicious.txt")
	keywords_mal = get_keyword_set(pdfs_mal)
	ni_mal = get_frequency_keywords(keywords_mal,pdfs_mal)
	print_to_csv("keywords_mal.csv",ni_mal)

	pdfs = list_of_pdfs("tree_struct_clean.txt")
	keywords = get_keyword_set(pdfs)
	ni = get_frequency_keywords(keywords,pdfs) 
	print_to_csv("keywords_clean.csv",ni)

	km = read_csv("keywords-mal-cluster.csv")
	kc = read_csv("keywords-clean-cluster.csv")
	k = km + kc
	k = ["File.*"] + k
	freq_mal =  (get_frequency_each_pdf(k,pdfs_mal))
	freq_clean = (get_frequency_each_pdf(k,pdfs))

	file_clean = open("frequency_clean.csv","a")
	final_keywords = freq_mal[0].keys()
	wr_clean = csv.writer(file_clean, quoting = csv.QUOTE_ALL)
	wr_clean.writerow(final_keywords)

	file_malicious = open("frequency_malicious.csv","a")
	final_keywords = freq_mal[0].keys()
	wr_malicious = csv.writer(file_malicious, quoting = csv.QUOTE_ALL)
	wr_malicious.writerow(final_keywords)

	for i in freq_clean:
		wr_clean.writerow(i.values())

	for i in freq_mal:
		wr_malicious.writerow(i.values())

# read_output()