import numpy as np
from sklearn import svm, preprocessing
from sklearn.metrics import precision_recall_fscore_support,accuracy_score
import pandas as pd
import random
import time

FEATURES = ["Size",
	"Indirect Objects",
	"Versions",
	"Streams",
	"Compressed Objects",
	"Object Streams",
	"JavaScript Objects",
	"Origami",
	"PeePDF",
	"/N",
	"/StructTreeRoot",
	"/Catalog",
	"/F",
	"/D",
	"/C",
	"/A",
	"/Outlines",
	"/FontDescriptor",
	"/P",
	"/Info",
	"/JavaScript",
	"/Page",
	"/ExtGState",
	"/Nums",
	"/Pages",
	"/Annot",
	"/O",
	"/Font",
	"/Pa",
	"/Action"]

def Build_Dataset():
	data_df = pd.DataFrame.from_csv("IAS_Features.csv", index_col=None)
	data_df = data_df.sample(n=len(data_df))
	X = np.array(data_df[FEATURES].values)
	X.astype(float)
	y = (data_df["Class"]
		.replace("Yes",1)
		.replace("No",0)
		.values.tolist())
	X = preprocessing.scale(X)
	fname = (data_df["Filename"].values.tolist())
	return X,y,fname

def Analysis():
	test_size = 5000
	X,y,fname = Build_Dataset()
	print len(X)

	clf = svm.SVC()
	clf.fit(X[:-test_size],y[:-test_size])
	correct_count = 0
	y_pred = []
	y_true=[]
	file = open("Wrongly_classified.txt","w")
	for x in range(1, test_size + 1):
		y_pred.append(clf.predict(X[-x])[0])
		y_true.append(y[-x])
		#if clf.predict(X[-x])[0] == y[-x]:
		if y_pred[x-1] != y_true[x-1]:
			file.write(fname[-x])
			file.write("\n\n")
	
	print "Accuracy", (100*accuracy_score(y_true,y_pred,normalize=True))
	print "Correctly classified", (accuracy_score(y_true,y_pred,normalize=False))
	print precision_recall_fscore_support(y_true, y_pred, average='binary')

Analysis()
