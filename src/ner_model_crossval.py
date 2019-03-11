import sys
from tqdm import tqdm
import numpy as np

from IPython.core import debugger
breakpoint = debugger.set_trace

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn import metrics
from sklearn.feature_selection import VarianceThreshold, SelectKBest, chi2
from sklearn.model_selection import KFold

sys.path.append('../utils')

import letterFeatures, posFeatures, ruleBasedFeatures, dictFeatures

import nltk
	
def generate_features(data):
	print("---------- Generating features ---------- ")
	X = []
	for index, row in tqdm(data.iterrows()):
		features = []

		#print("row : ", row)
		
		# Generate Letter Fetures

		#features.append(letterFeatures.firstLetterCapital(row))
		features.append(letterFeatures.allCapitals(row))
		#features.append(letterFeatures.allLower(row))
		features.append(letterFeatures.isFirstLetterAlphabet(row))
		#features.append(letterFeatures.containsDigits(row))
		features.append(letterFeatures.stringLen(row))
		features.append(letterFeatures.numWords(row))
		features.append(letterFeatures.isFirstLetterofAnyWordCapital(row))
		features.append(letterFeatures.doesTheStringContainQuotes(row))
		features.append(letterFeatures.isItPrecededByThe(row))
		features.append(letterFeatures.numberOfVowels(row))
		features.append(letterFeatures.nextWordISsaid(row))
		features.append(letterFeatures.isItPrecededByIn(row))
		features.append(letterFeatures.isFirstLetterofEveryWordCapital(row))
		features.append(letterFeatures.nextWordIsHas(row))
		features.append(letterFeatures.isTheFirstWordCapsNew(row))
		features.append(letterFeatures.isThePrevWordCapsNew(row))
		features.append(letterFeatures.isThePrevWordADirection(row))
		features.append(letterFeatures.isTheFirstWordADirection(row))

		# POS Tagging Features
		features += posFeatures.posCounts(row)
		features += posFeatures.posCountsNGram(row) # 1-gram

		# Rule based features
		features.append(ruleBasedFeatures.wordContainsDayOfWeek(row))
		features.append(ruleBasedFeatures.wordContainsMonth(row))
		#features.append(ruleBasedFeatures.prevWordContainsDirection(row))
		#features.append(ruleBasedFeatures.wordContainsDirection(row))

		#dictionary features
		features.append(dictFeatures.dictionaryTwoLetterCapitalWordexceptUSUKEU(row))

		X.append(features)

		
	X = np.asarray(X)
	print("Total number of features : ", X.shape[1], "\n")

	return X

def feature_selection(X, Y, method):
	print("---------- Performing feature selection using", method, " ---------- ", )
	if method == 'threshold':
		sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
		X = sel.fit_transform(X)
	elif method == 'select-k-best':
		sel = SelectKBest(score_func=chi2, k=130)
		X = sel.fit_transform(X, Y)

	print("Number of features selected : ", X.shape[1], "\n")
	return X

def create_grid_for_CV():
	# No. of trees in random forest
	n_estimators = [int(x) for x in np.linspace(start = 50, stop = 500, num = 50)]

	# No. of features to consider at every split
	max_features = ['auto', 'sqrt']

	# Max number of levels in tree
	max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
	max_depth.append(None)
	# Min number of samples required to split a node
	min_samples_split = [2, 5, 10]

	# Min number of samples required at each leaf node
	min_samples_leaf = [1, 2, 4]

	# Method of selecting samples for training each tree
	bootstrap = [True, False]
	
	random_grid = {'n_estimators': n_estimators,
				   'max_features': max_features,
				   'max_depth': max_depth,
				   'min_samples_split': min_samples_split,
				   'min_samples_leaf': min_samples_leaf,
				   'bootstrap': bootstrap}
	
	return random_grid
	
def training(X_train, Y_train, method, random_grid=None):
	print("---------- Building model ----------")

	if method == "Logistic Regression":
		model = LogisticRegression(C=1, penalty='l2', solver='liblinear', max_iter=500)
		model.fit(X_train, Y_train)
	elif method == "Support Vector Machine":
		model = SVC(gamma='auto', C=0.9)
		model.fit(X_train, Y_train) 
	elif method == "Decision Tree Classifier":
		model = DecisionTreeClassifier()
		model.fit(X_train, Y_train)
	elif method == "Random Forest":
		model = RandomForestClassifier(n_estimators=100, max_depth=None, min_samples_split=2, random_state=0)
		if random_grid is None:
			model.fit(X_train, Y_train)
		else:
			rf_random = RandomizedSearchCV(estimator = model, param_distributions = random_grid, n_iter = 10, cv = 3, verbose=2, random_state=42, n_jobs = -1)
			rf_random.fit(X_train, Y_train)
			print(rf_random.best_params_)
			model = rf_random
	else:
		print("Incorrect Input")
	return model

def post_processing(X_test, Y_test, Y_pred):
	pass

def evaluate_model(X_test, Y_test, model):
	Y_pred = model.predict(X_test)


	false_neg_idx = np.where((Y_test==1) & (Y_pred==0)) # False Negative

	false_pos_idx = np.where((Y_pred==1) & (Y_test==0)) # False Positive

	# Before Post-processing
	accuracy = metrics.accuracy_score(Y_test, Y_pred)
	precision = metrics.precision_score(Y_test, Y_pred) # tp/(tp+fp)
	recall = metrics.recall_score(Y_test, Y_pred) # tp/(tp+fn)
	f1_score = metrics.f1_score(Y_test, Y_pred)
	# print("accuracy : ", accuracy)  
	# print("Precision : ", precision)
	# print("Recall : ", recall)
	# print("f1-score : ", f1_score)
	# print("")

	return (accuracy, precision, recall, f1_score, false_pos_idx, false_neg_idx)

# def cross_validation(data, kfolds=2, method="Random Forest"):


def build_ner_model(X, Y, method):
	print("----------",method,"----------")
	print("---------- Training Phase ----------")

	# Creating Grid for CV - Set it to None, if not using.
	result_folder = '../result/crossval/'
	
	accuracy_all = np.array([])
	precision_all = np.array([])
	recall_all = np.array([])
	f1_score_all = np.array([])

	kf = KFold(n_splits=5)
	for train_index, val_index in kf.split(X):
		# print("TRAIN:", train_index, "TEST:", val_index)
		# print("TRAIN:", train_index, "TEST:", val_index)
		X_train, X_val = X[train_index], X[val_index]
		Y_train, Y_val = Y[train_index], Y[val_index]

		# Training model
		model = training(X_train, Y_train, method)
		
		# Evaluating the model with training data
		(accuracy, precision, recall, f1_score, false_pos_idx, false_neg_idx) = evaluate_model(X_val, Y_val, model)
		accuracy_all = np.append(accuracy_all, accuracy )
		precision_all = np.append(precision_all, precision )
		recall_all = np.append(recall_all, recall )
		f1_score_all = np.append(f1_score_all, f1_score )
	
	# false_pos_idx, false_neg_idx = evaluate_model(X_train, Y_train, model)
	# data_train.iloc[false_pos_idx[0], :].reset_index(drop=True).to_pickle(result_folder+method+'_false_pos_train.pkl')
	# data_train.iloc[false_neg_idx[0], :].reset_index(drop=True).to_pickle(result_folder+method+'_false_neg_train.pkl')


	print("Cross-Validation Results for {}".format(method))
	print("		Mean accuracy : ", np.mean(accuracy_all))  
	print("		Mean Precision : ", np.mean(precision_all))
	print("		Mean Recall : ", np.mean(recall_all))
	print("		Mean f1-score : ", np.mean(f1_score_all))






	#breakpoint()


