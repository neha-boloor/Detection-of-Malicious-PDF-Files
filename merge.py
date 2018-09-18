from pprint import pprint
import csv
import os

def read_csv(filename):
	dataset = list()
	file = open(filename,'r')
	csv_reader = csv.reader(file)
	for row in csv_reader:
		dataset.append(row)
	return dataset

def merge():
	object_clean = read_csv("frequency_clean.csv")
	object_malicious = read_csv("frequency_malicious.csv")
	struct_clean = read_csv("gen_struct_clean.csv")
	struct_malicious = read_csv("gen_struct_malicious.csv")
	peepdf_clean = read_csv("peepdf_clean.csv")
	peepdf_malicious = read_csv("peepdf_mal.csv")
	origami_clean = read_csv("origami_1_beta1/sources/scripts/scan/origami_clean.csv")
	origami_malicious = read_csv("origami_1_beta1/sources/scripts/scan/origami_malicious.csv")

	file = open("Features.csv",'a')
	file_clean = open("Features_clean.csv",'a')
	file_malicious = open("Features_malicious.csv",'a')
	wr = csv.writer(file, quoting = csv.QUOTE_ALL)
	wr_clean = csv.writer(file_clean, quoting = csv.QUOTE_ALL)
	wr_malicious = csv.writer(file_malicious, quoting = csv.QUOTE_ALL)

	for i in range(len(object_clean)):
		temp = struct_clean[i] + [peepdf_clean[i][1]] + [origami_clean[i][1]] + object_clean[i][1:]
		wr_clean.writerow(temp)
		wr.writerow(temp)

	for i in range(len(object_malicious)):
		temp = struct_malicious[i] + [peepdf_malicious[i][1]] + [origami_malicious[i][1]] + object_malicious[i][1:]
		wr_malicious.writerow(temp)
		wr.writerow(temp)

# merge()
# file_path = "./Run1/"
# directory = os.path.dirname(file_path)
# if not os.path.exists(directory):
#     os.makedirs(directory)