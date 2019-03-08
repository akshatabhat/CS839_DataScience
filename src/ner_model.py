import sys
import pickle
from tqdm import tqdm

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve

sys.path.append('../utils')

import letterFeatures



def load_data(input_filename):
	print("---------- Loading the data ---------- ")
	print("Data filename : ", input_filename)
	f = open(input_filename, 'rb')
	data = pd.read_pickle(f)
	return data
	
def generate_features(data):
	print("---------- Generating features ---------- ")
	X = []
	for index, row in tqdm(data.iterrows()):
		features = []
		#Generate Letter Fetures
		features.append(letterFeatures.firstLetterCapital(row))
		features.append(letterFeatures.allCapitals(row))
		features.append(letterFeatures.allLower(row))
		features.append(letterFeatures.isFirstLetterAlphabet(row))
		features.append(letterFeatures.containsDigits(row))
		features.append(letterFeatures.stringLen(row))

		# Other features


		X.append(features)

	return X


def training(X, Y):
	print("---------- Training model ----------")
	X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.33)
	logreg = LogisticRegression(C=1e5, solver='lbfgs')
	logreg.fit(X_train, Y_train)
	Y_pred = logreg.predict(X_val)
	precision, recall, thresholds = precision_recall_curve(Y_val, Y_pred)

	print("Precision = ", precision)
	print("Recall = ", recall)
	print("thresholds = ", thresholds)


if __name__ == '__main__':
	
	# Load and read data into dataframe
	input_filename = '../data/data_window_ngram-5.pkl'
	data = load_data(input_filename)

	X = generate_features(data)

	Y = data['labels']
	Y=Y.astype('int')
	training(X, Y)

	# model evaluation
