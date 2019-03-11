import pandas as pd
import pickle
import math
import re

regex = re.compile('[^a-zA-Z]')


def dictionaryTwoLetterCapitalWordexceptUSUKEU(data):
	word = str(data["word"])
	prev = str(data["prev4"])
	bl = ['the', 'to', 'at', 'and', 'in', 'of']
	if (word[0].isalpha() == False):
		word = word[1:]
	if (len(word) == 2) :
		if (word.isupper() == True) :
			if (word == "US") :
				return 0
			elif (word == "UK") :
				return 0
			elif (word == "EU") :
				return 0
			elif (word == "NZ") :
				return 0
			elif (word == "SA") :
				return 0
			else :
				return 1
		else :
			return 0		
	elif (word[0:2].isupper() == True) :
		if (len(word) > 2) :
		    if (word[2].isalpha() == False) :
		    	if (word[0:2] == "US") :
		    		return 0
		    	elif (word[0:2] == "UK") :
		    		return 0
		    	elif (word[0:2] == "EU") :
		    		return 0
		    	elif (word[0:2] == "NZ") :
		    		return 0
		    	elif (word[0:2] == "SA") :
		    		return 0
		    	else :
		    		return 1
		return 0
	elif prev in bl:
		return 1
	return 0


def whitelist(X_test, Y_pred, false_neg_idx, data):
	#breakpoint()
	for idx in false_neg_idx[0]:
			word = str(data.iloc[idx]["word"])
			word = regex.sub('',word)
			word = word.upper()
			if 'US' in word:
				Y_pred[idx] = 1
			elif 'U.S.' in word :
				Y_pred[idx] = 1
			elif 'UK' in word :
				Y_pred[idx] = 1
			elif 'EU' in word :
				Y_pred[idx] = 1
			elif 'INDIA' in word :
				Y_pred[idx] = 1
			elif 'CHINA' in word :
				Y_pred[idx] = 1
			elif 'GERMANY' in word:
				Y_pred[idx] = 1
	return Y_pred

'''
f = open('../data/data_window_ngram-5.pkl', 'rb')
data = pd.read_pickle(f)
f.close()
#print(data.iloc[0])
#print("%20s | %20s  | %20s | %5s | %3s" %("previous word", "word", "next word", "label", "file_ids"))
print("%20s | %5s | %3s" %("word", "label", "file_ids"))
for index, row in data.iterrows():
	word = str(row["word"])
	if (word[0:2].isupper() == True):
		if(dictionaryTwoLetterCapitalWordexceptUSUKEU(data.iloc[index]) == 0):
			print(row["word"])
		#print("%20s | %20s  | %20s | %5s | %3d" %(row["prev4"], row["word"], row["after0"], row["labels"], row["file_ids"]))
		#print("%20s | %5s | %3d" %(row["word"], row["labels"], row["file_ids"]))
'''