import csv
from pprint import pprint
import math
import random
import numpy
import math
	
random.seed(1)
def read_csv(filename):
	dataset = list()
	file = open(filename,'r')
	csv_reader = csv.reader(file)
	first_row = True
	for row in csv_reader:
		if first_row:
			first_row = False
			continue
		dataset.append(row[:])
	string_to_float(dataset)
	return dataset

def string_to_float(dataset):
	for row in dataset:
		for column in range(len(row)-1):
			if type(row[column]) != type(int(4)):
				row[column] = float(row[column].strip())

def euclidean_diatance(x,y):
	sum_of_squares = 0
	for i in range(len(x)-1):
		sum_of_squares += (x[i]-y[i])**2
	return math.sqrt(sum_of_squares)

def find_cluster(dataset,cluster_centers):
	cluster = []
	for i in range(len(cluster_centers)):
		temp = []
		cluster.append(list(temp))
	for i in range(len(dataset)):
		dist_from_center = []
		for j in range(len(cluster_centers)):
			dist_from_center.append(euclidean_diatance(dataset[i],cluster_centers[j]))
		min_index = dist_from_center.index(min(dist_from_center))
		cluster[min_index].append(dataset[i])
	return cluster

def reeval_center(cluster_centers, cluster):
	new_center = []
	temp_clusters = []
	for i in range(len(cluster)):
		temp = []
		for j in cluster[i]:
			temp.append(j[:len(j)-1])
		temp_clusters.append(temp)
	for i in range(len(cluster)):
		new_center.append(numpy.mean(temp_clusters[i],axis=0).tolist())
	return new_center

def _kmeans(dataset,k_clusters):
	cluster_centers = []
	temp = random.sample(range(len(dataset)),k_clusters)
	for i in temp:
		cluster_centers.append(dataset[i][:len(dataset[0])-1])
	cluster = find_cluster(dataset,cluster_centers)
	new_centers = reeval_center(cluster_centers, cluster)
	count = 1
	while cluster_centers!=new_centers and count<100:
		cluster_centers = new_centers
		cluster = find_cluster(dataset,cluster_centers)
		new_centers = reeval_center(cluster_centers, cluster) 
		print "ITERATION ",count
		print "Cluster 0 has ",len(cluster[0]),"tuples"
		print "Cluster 1 has ",len(cluster[1]),"tuples\n"
		count = count + 1

	analysis = dict()
	print ""
	for i in range(len(cluster)):
		count_yes = 0
		count_no = 0
		count_dict = dict()
		for j in cluster[i]:
			if j[-1] == "No" or j[-1]=="NO" or j[-1]=="no":
			#if j[-1] == "Iris-setosa":
				count_no += 1
			else:
				count_yes +=1
		count_dict["Cluster Number"] = i
		count_dict["No"] = count_no
		count_dict["Yes"] = count_yes
		maximum = max(count_dict, key=count_dict.get) 
		count_dict["Class"] = maximum
		analysis[i] = count_dict

		if count_dict["Class"] == "Yes":
			true_positive = count_dict["Yes"]
			false_negative = count_dict["No"]
		else:
			true_negative = count_dict["No"]
			false_positive = count_dict["Yes"]
	
	print "\nSelected Keywords are:\n"
	if len(cluster[0]) > len(cluster[1]):
		pprint(cluster[1])
		print "\n"
		return cluster[1],cluster[0]
	else:
		pprint(cluster[0])
		print "\n"
		return cluster[0],cluster[1]
	
def write_to_csv(selected,rejected,file_type):
	file = open("keywords_"+str(file_type)+"_clustered.csv",'a')
	wr = csv.writer(file, quoting = csv.QUOTE_ALL)
	for i in selected:
		i = i + ["cluster1"]
		wr.writerow(i)
	for i in rejected:
		i = i + ["cluster0"]
		wr.writerow(i)


def kmeans(ftype):
	if ftype:
		file_type = "malicious"
		filename = "keywords_malicious.csv"
	else:
		file_type = "clean"	
		filename = "keywords_clean.csv"
	dataset = read_csv(filename)
	selected, rejected = _kmeans(dataset,2)
	write_to_csv(selected,rejected,file_type)

kmeans(1)