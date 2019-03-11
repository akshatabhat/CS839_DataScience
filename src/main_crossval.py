import sys
import ner_model_crossval
import pandas as pd
import numpy as np
import pickle
import preprocessing
import argparse

def load_data(input_filename):
	print("---------- Loading the data ---------- ")
	print("Data filename : ", input_filename)
	f = open(input_filename, 'rb')
	data = pd.read_pickle(f)
	print("") 
	return data
	

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	# Load and read data into pandas dataframe
	input_filename = '../Data/data_window_ngram-5.pkl'
	data = load_data(input_filename)
	# data = data[data['file_ids'] < 300].reset_index()
	# data_train = data[data['file_ids'] < 220].reset_index()
	# data_test = data[data['file_ids'] >= 220].reset_index()

	data_train = data[data['file_ids'] < 311].reset_index(drop=True)
	print("Training data size : ", data_train.shape[0])
	# Preprocessing
	processed_data_train = preprocessing.preprocessing(data_train)
	print("Pre-processed training data size : ", data_train.shape[0])

	# Generate feature matrix
	X = ner_model_crossval.generate_features(data_train)
	Y = data_train['labels'].astype(int).as_matrix()
	print("Class Distribution of training data : ", np.unique(Y, return_counts = True)), "\n"

	# Build Named Entity Recognizer.
	ner_model_crossval.build_ner_model(X, Y, "Logistic Regression")
	ner_model_crossval.build_ner_model(X, Y, "Random Forest")
	ner_model_crossval.build_ner_model(X, Y, "Decision Tree Classifier")
	ner_model_crossval.build_ner_model(X, Y, "Support Vector Machine")

