import pandas as pd
import pickle

def firstLetterCapital(data):
	word = str(data["word"])
	return word[0].isupper() 

def allCapitals(data):
	word = str(data["word"])
	return word.isupper()

def allLower(data):
	word = str(data["word"])
	return word.islower()


def isFirstLetterAlphabet(data):
	word = str(data["word"])
	return word[0].isalpha()	

def containsDigits(data):
	word = str(data["word"])
	for i in word:
		if (i.isdigit() == True):
			return True
	return False

def stringLen(data):
	word = str(data["word"])
	return len(word)


f = open('../data/data_window_ngram-5.pkl', 'rb')
data = pd.read_pickle(f)
f.close()
row = data.iloc[0]
print(allLower(row))
row = data.iloc[1]
print(stringLen(row))