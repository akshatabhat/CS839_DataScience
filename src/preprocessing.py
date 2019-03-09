import pandas as pd
import pickle
import sys
from tqdm import tqdm
sys.path.append('../utils')
import letterFeatures

def preprocessing(data):
	print("---------- Pre-processing ----------")
	drop_index = []
	for index, row in tqdm(data.iterrows()):
		if (letterFeatures.allLower(row) == 1):
			drop_index.append(index)
		elif (letterFeatures.isFirstLetterofAnyWordCapital(row) == 0):
			drop_index.append(index)
	data.drop(drop_index, inplace=True)
	return data

#f = open('../data/data_window_ngram-5.pkl', 'rb')
#data = pd.read_pickle(f)
#f.close()
#data = preprocessing(data)
#print(data)