import pandas as pd
import pickle
import sys
from tqdm import tqdm
sys.path.append('../utils')
import letterFeatures

def posOfFullStop(data):
	pos = 0
	word = str(data["word"])
	for char in word:
		pos += 1
		if "." in char:
			return pos
	return 0

def preprocessingOld(data):
	print("---------- Pre-processing ----------")
	drop_index = []
	for index, row in tqdm(data.iterrows()):
		if (letterFeatures.allLower(row) == 1):
			drop_index.append(index)
		elif (letterFeatures.isFirstLetterofAnyWordCapital(row) == 0):
			drop_index.append(index)
	data.drop(drop_index, inplace=True)
	return data

def preprocessing(data):
	print("---------- Pre-processing ----------")
	drop_index = []
	for index, row in tqdm(data.iterrows()):
		if (letterFeatures.allLower(row) == 1):
			drop_index.append(index)
		elif (letterFeatures.isFirstLetterofAnyWordCapital(row) == 0):
			drop_index.append(index)
		elif (letterFeatures.containsDigits(row) == 1):
			drop_index.append(index)
		elif (letterFeatures.stringLen(row) == 1):
			drop_index.append(index)
		elif (letterFeatures.stringLen(row) == 2):
			if (letterFeatures.allCapitals(row) == 0):
				drop_index.append(index)
		elif (row["word"] == "A"):
			drop_index.append(index)
		elif (row["word"] == "An"):
			drop_index.append(index)
		elif (row["word"] == "The"):
			drop_index.append(index)
		elif (row["word"] == '"The'):
			drop_index.append(index)
		elif (row["word"] == "And"):
			drop_index.append(index)
		elif (letterFeatures.stringContainsFullStop(row) == 1):
			pos = posOfFullStop(row)
			len = letterFeatures.stringLen(row)
			if (pos != len):
				if (letterFeatures.allCapitals(row) == 0):
					drop_index.append(index)
		#containsDigits
		#singleletter
		#two letter words which are not all caps
		#word is an article like A, An, The
		#connectors like and
		#if fullstop is not the last char and not everything is capital (like U.S.)
	data.drop(drop_index, inplace=True)
	return data

'''
f = open('../data/data_window_ngram-5.pkl', 'rb')
data = pd.read_pickle(f)
f.close()
data = preprocessingBeta(data)
for index, row in data.iterrows():
	print(row["word"])
'''