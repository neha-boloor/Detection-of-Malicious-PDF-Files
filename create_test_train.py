import csv

def read_csv(filename):
	dataset = list()
	header = None
	file = open(filename,'r')
	csv_reader = csv.reader(file)
	first = True
	for row in csv_reader:
		if first:
			header = row
			first = False
			continue
		dataset.append(row)
	return dataset,header


file_train = open("TRAIN.csv",'a')
wr_train = csv.writer(file_train, quoting = csv.QUOTE_ALL)
file_test = open("TEST.csv",'a')
wr_test = csv.writer(file_test, quoting = csv.QUOTE_ALL)

pdfs_clean,header = read_csv("Features_clean.csv")
train_len_clean = len(pdfs_clean) * 0.7
pdfs_malicious,header = read_csv("Features_malicious.csv")
train_len_malicious = len(pdfs_malicious) * 0.7

wr_test.writerow(header)
wr_train.writerow(header)

for i in range(len(pdfs_clean)):
	if i <= train_len_clean:
		wr_train.writerow(pdfs_clean[i])
	else:
		wr_test.writerow(pdfs_clean[i])

for i in range(len(pdfs_malicious)):
	if i <= train_len_malicious:
		wr_train.writerow(pdfs_malicious[i])
	else:
		wr_test.writerow(pdfs_malicious[i])
