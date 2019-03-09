import pandas as pd
#import pickle
import sys
from tqdm import tqdm
sys.path.append('../utils')
import letterFeatures

def preprocessing(data):
	print("---------- Pre-processing ----------")
	for index, row in tqdm(data.iterrows()):
		if (letterFeatures.allLower(row) == 1):
			data.drop([index], inplace=True)
	return data

#f = open('../data/data_window_ngram-5.pkl', 'rb')
#data = pd.read_pickle(f)
#f.close()
#print(preprocessing(data[:1000]))