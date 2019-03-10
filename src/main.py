import sys
import ner_model
import pandas as pd
import pickle
import preprocessing
import argparse
from IPython.core import debugger
breakpoint = debugger.set_trace

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
	data = data[data['file_ids'] < 110].reset_index()
	data_train = data[data['file_ids'] < 80].reset_index()
	data_test = data[data['file_ids'] >= 80].reset_index()

	# data_train = data[data['file_ids'] < 400].reset_index()
	# data_test = data[data['file_ids'] >= 400].reset_index()

	print("Training data size : ", data_train.shape[0], ", Test data size : ",data_test.shape[0])
	# Preprocessing
	processed_data_train = preprocessing.preprocessing(data_train)

	processed_data_test = preprocessing.preprocessing(data_test)

	# processed_data_filename = "../data/data_window_ngram-5-processed.pkl"
	# print("Saving pre-processed data to ", processed_data_filename)
	# processed_data.to_pickle(processed_data_filename)

	# Build Named Entity Recognizer.
	# ner_model.build_ner_model(processed_data_train, processed_data_test, "Logistic Regression")
	#ner_model.build_ner_model(processed_data, "Support Vector Machine")
	ner_model.build_ner_model(processed_data_train, processed_data_test, "Random Forest")
	# ner_model.build_ner_model(processed_data_train, processed_data_test, "Decision Tree Classifier")

