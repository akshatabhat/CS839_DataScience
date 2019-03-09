import sys
import ner_model
import pandas as pd
import pickle
import preprocessing

def load_data(input_filename):
	print("---------- Loading the data ---------- ")
	print("Data filename : ", input_filename)
	f = open(input_filename, 'rb')
	data = pd.read_pickle(f)
	print("")
	return data
	

if __name__ == '__main__':
	
	# Load and read data into pandas dataframe
	input_filename = '../data/data_window_ngram-5.pkl'
	data = load_data(input_filename)

	# Preprocessing
	processed_data = preprocessing.preprocessing(data)

	# Build Named Entity Recognizer.
	ner_model.build_ner_model(processed_data)


