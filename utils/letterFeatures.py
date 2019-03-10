import pandas as pd
import pickle
import math

def firstLetterCapital(data):
	word = str(data["word"])
	if (word[0].isalpha() == False) :
			if (len(word) > 1) :
				if (word[1].isupper() == True):
					return 1	
			elif (word[0].isupper() == True):
				return 1
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

def doesTheStringContainQuotes(data):
	word = str(data["word"])
	for char in word:
		if '"' in char:
			return 1
	return 0

def isItPrecededByThe(data):
	prevWord = str(data["prev4"])
	if ("the" == prevWord):
		return 1
	if ("The" == prevWord):
		return 1
	return 0

def numberOfVowels(data):
	word = str(data["word"])
	count = 0
	for char in word:
		if ("a" == char) :
			count += 1
		elif ("e" == char) :
			count += 1
		elif ("i" == char) :
			count += 1
		elif ("o" == char) :
			count += 1
		elif ("u" == char) :
			count += 1
	return count

def stringContainsFullStop(data):
	word = str(data["word"])
	for char in word:
		if "." in char:
			return 1
	return 0

def endsWithColon(data):
	word = str(data["word"])
	if (word[len(word) - 1] == ":"):
		return 1
	else :
		return 0


def endsWithQuoteS(data):
	word = str(data["word"])
	if (word[len(word) - 2:len(word)] == "'s"):
		return 1
	else :
		return 0

def nextWordISsaid(data):
	word = str(data["after0"])
	if (word == "said") :
		return 1
	else :
		return 0		

def isItPrecededByIn(data):
	prevWord = str(data["prev4"])
	if ("in" == prevWord):
		return 1
	if ("In" == prevWord):
		return 1
	return 0

def isFirstLetterofEveryWordCapital(data):
	words = str(data["word"])
	words = words.split(" ")
	for word in words:
		if (word[0].isalpha() == False) :
			if (len(word) > 1) :
				if (word[1].isalpha() == False):
					return 0
				else :
					if (word[1].islower() == True):
						return 0
			else:
				return 0	
		elif (word[0].islower() == True):
			return 0
	return 1

#next word is "has"
'''
f = open('../data/data_window_ngram-5.pkl', 'rb')
data = pd.read_pickle(f)
f.close()
print(data.iloc[0])
for index, row in data.iterrows():
	if(isFirstLetterofEveryWordCapital(row)):
		print("%s" %(row["word"]))
'''