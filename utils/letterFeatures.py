import pandas as pd
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

def numWords(data):
	words = str(data["word"])
	words = words.split(" ")
	return len(words)

def isFirstLetterofAnyWordCapital(data):
	words = str(data["word"])
	words = words.split(" ")
	for word in words:
		if (word[0].isalpha() == False) :
			if (len(word) > 1) :
				if (word[1].isupper() == True):
					return 1	
		elif (word[0].isupper() == True):
			return 1
	return 0

#f = open('../data/data_window_ngram-5.pkl', 'rb')
#data = pd.read_pickle(f)
#f.close()
#print(data)
#row = data.iloc[1]
#print(row["word"])
#print(isFirstLetterofAnyWordCapital(row))
#row = data.iloc[368680]
#print(row["word"])
#print(isFirstLetterofAnyWordCapital(row))