import sys
import pickle
from tqdm import tqdm

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn import metrics

sys.path.append('../utils')

import letterFeatures, posFeatures
import nltk
nltk.download('averaged_perceptron_tagger')

def load_data(input_filename):
	print("---------- Loading the data ---------- ")
	print("Data filename : ", input_filename)
	f = open(input_filename, 'rb')
	data = pd.read_pickle(f)
	print("")
	return data
	
def generate_features(data):
	print("---------- Generating features ---------- ")
	X = []
	for index, row in tqdm(data.iterrows()):
		features = []

		#print("row : ", row)
		
		# Generate Letter Fetures
		features.append(letterFeatures.firstLetterCapital(row))
		features.append(letterFeatures.allCapitals(row))
		features.append(letterFeatures.allLower(row))
		features.append(letterFeatures.isFirstLetterAlphabet(row))
		features.append(letterFeatures.containsDigits(row))
		features.append(letterFeatures.stringLen(row))

		# POS Tagging Features
		#features.append(posFeatures.posCounts(data))
		#features.append(posFeatures.posCountsNGram(data)) # 1-gram


		X.append(features)

	print("")	
	return np.asarray(X)


def training(X_train, Y_train, method):
	print("---------- Training model using", method ,"----------")

	if method == "Logistic Regression":
		model = LogisticRegression(C=1e5, solver='lbfgs')
		model.fit(X_train, Y_train)
	elif method == "Support Vector Machine":
		model = SVC(gamma='scale')
		model.fit(X_train, Y_train) 
	elif method == "Decision Tree Classifier":
		model = DecisionTreeClassifier()
		model.fit(X_train, Y_train)
	elif method == "Random Forest":
		model = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
		model.fit(X_train, Y_train)
	else:
		print("Incorrect Input")
	return model

def evaluate_model(X_test, Y_test, model):
	Y_pred = model.predict(X_test)
	accuracy = metrics.accuracy_score(Y_test, Y_pred)
	precision = metrics.precision_score(Y_test, Y_pred) # tp/(tp+fp)
	recall = metrics.recall_score(Y_test, Y_pred) # tp/(tp+fn)
	f1_score = metrics.f1_score(Y_test, Y_pred)
	print("accuracy : ", accuracy)  
	print("Precision : ", precision)
	print("Recall : ", recall)
	print("f1-score : ", f1_score)

if __name__ == '__main__':
	
	# Load and read data into pandas dataframe
	input_filename = '../data/data_window_ngram-5.pkl'
	data = load_data(input_filename)

	# Generate feature matrix
	X = generate_features(data)
	Y = data['labels'].astype(int)
	print("Class Distribution : \n", np.unique(Y, return_counts = True))

	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33) #TODO

	# Training model
	model = training(X_train, Y_train, "Logistic Regression")

	# Evaluting the model
	evaluate_model(X_test, Y_test, model)
