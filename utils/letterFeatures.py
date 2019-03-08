#import pandas as pd
#import pickle

def firstLetterCapital(data):
	word = str(data["word"])
	if (word[0].isupper() == True) :
		return 1
	else :
		return 0 

def allCapitals(data):
	word = str(data["word"])
	if (word.isupper() == True) :
		return 1
	else :
		return 0

def allLower(data):
	word = str(data["word"])
	if (word.islower() == True) :
		return 1
	else :
		return 0

def isFirstLetterAlphabet(data):
	word = str(data["word"])
	if (word[0].isalpha() == True) :
		return 1
	else :
		return 0	

def containsDigits(data):
	word = str(data["word"])
	for i in word:
		if (i.isdigit() == True):
			return 1
	return 0

def stringLen(data):
	word = str(data["word"])
	return len(word)


#f = open('../data/data_window_ngram-5.pkl', 'rb')
#data = pd.read_pickle(f)
#f.close()
#row = data.iloc[0]
#print(allLower(row))
#row = data.iloc[1]
#print(allLower(row))