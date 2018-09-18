import re
from pprint import pprint
import csv

def list_of_pdfs(filename):
	f = open(filename)
	temp = ""
	pdfs = []
	for line in f.readlines():
		if line.strip() == "#":
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
		outfile.write("keyword")
		outfile.write(",frequency")
		outfile.write("\n")
		for k,v in ni.items():
			outfile.write(str(k))
			outfile.write(","+str(v))
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
		freq = dict()
		for j in keywords:
			if j=="File.*":
				fname = (re.search(j,i)).group(0).split(' ')[1]
				freq["Filename"] = fname
			else:
				freq[j] = len(re.findall(j,i))
		freq_each_pdf.append(freq)
	return freq_each_pdf

pdfs_mal = list_of_pdfs("tree-gen-output-mal.txt")
# keywords_mal = get_keyword_set(pdfs_mal)
# ni_mal = get_frequency_keywords(keywords_mal,pdfs_mal)
# print_to_csv("keywords-mal.csv",ni_mal)

pdfs = list_of_pdfs("tree-gen-output-clean.txt")
# keywords = get_keyword_set(pdfs)
# ni = get_frequency_keywords(keywords,pdfs) 
# print_to_csv("keywords-clean.csv",ni)

km = read_csv("keywords-mal-cluster.csv")
kc = read_csv("keywords-clean-cluster.csv")
k = km + kc
k = ["File.*"] + k
freq_mal =  (get_frequency_each_pdf(k,pdfs_mal))
freq_clean = (get_frequency_each_pdf(k,pdfs))
print freq_mal[0]

file = open("frequency-clean.csv","a")
k_mal = freq_mal[0].keys()
wr = csv.writer(file, quoting = csv.QUOTE_ALL)
wr.writerow(k_mal)

for i in freq_clean:
	wr.writerow(i.values())
