import sys
import ner_model
import pandas as pd
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
	input_filename = '../data/data_window_ngram-5.pkl'
	data = load_data(input_filename)

	# Preprocessing
	processed_data = preprocessing.preprocessing(data)

	processed_data_filename = "../data/data_window_ngram-5-processed.pkl"
	# print("Saving pre-processed data to ", processed_data_filename)
	# processed_data.to_pickle(processed_data_filename)

	# Build Named Entity Recognizer.
	ner_model.build_ner_model(processed_data, "Logistic Regression")
	ner_model.build_ner_model(processed_data, "Random Forest")
	ner_model.build_ner_model(processed_data, "Decision Tree Classifier")


