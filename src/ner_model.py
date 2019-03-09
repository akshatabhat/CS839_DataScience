import sys
from tqdm import tqdm
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_selection import VarianceThreshold, SelectKBest, chi2

sys.path.append('../utils')

import letterFeatures, posFeatures

import nltk
nltk.download('averaged_perceptron_tagger')
	
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

		features.append(letterFeatures.numWords(row))
		features.append(letterFeatures.isFirstLetterofAnyWordCapital(row))
		features.append(letterFeatures.doesTheStringContainQuotes(row))
		features.append(letterFeatures.isItPrecededByThe(row))
		features.append(letterFeatures.numberOfVowels(row))

		# POS Tagging Features

		features += posFeatures.posCounts(row)
		features += posFeatures.posCountsNGram(row) # 1-gram

		X.append(features)

		
	X = np.asarray(X)
	print("Total number of features : \n", X.shape[1])

	return X

def feature_selection(X, Y, method):
	print("---------- Performing feature selection using", method, " ---------- ", )
	if method == 'threshold':
		sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
		X = sel.fit_transform(X)
	elif method == 'select-k-best':
		sel = SelectKBest(score_func=chi2, k=130)
		X = sel.fit_transform(X, Y)

	print("Number of features selected : \n", X.shape[1])
	return X

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

def build_ner_model(data, method):

	# Generate feature matrix
	X = generate_features(data)
	Y = data['labels'].astype(int)
	print("Class Distribution : \n", np.unique(Y, return_counts = True))

	# Feature Selection
	#X = feature_selection(X, Y, 'select-k-best')

	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33) #TODO

	# Training model
	model = training(X_train, Y_train, method)

	# Evaluting the model
	evaluate_model(X_test, Y_test, model)

