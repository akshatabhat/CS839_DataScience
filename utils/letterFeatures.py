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

def nextWordIsHas(data):
	word = str(data["after0"])
	if (word == "has") :
		return 1
	elif (word == "Has") :
		return 1
	if (word == "has,") :
		return 1
	elif (word == "Has,") :
		return 1
	if (word == "has.") :
		return 1
	else :
		return 0

def isTheFirstWordCapsNew(data):
	word = str(data["word"])
	word = word.split(" ")
	if (len(word) == 2):
		if (word[0] == "New") :
			return 1
	return 0		

def isThePrevWordCapsNew(data):
	word = str(data["word"])
	word = word.split(" ")
	if (len(word) == 1):
		prevWord = str(data["prev4"])
		if (prevWord == "New") :
			return 1
	return 0		

def isThePrevWordADirection(data):
	word = str(data["prev4"])
	if "North" in word[0:5]:
		return 1
	elif "north" in word[0:5]:
		return 1
	elif "South" in word[0:5]:
		return 1
	elif "south" in word[0:5]:
		return 1
	elif "East" in word[0:4]:
		return 1
	elif "east" in word[0:4]:
		return 1
	elif "West" in word[0:4]:
		return 1
	elif "west" in word[0:4]:
		return 1
	return 0	

def isTheFirstWordADirection(data):
	word = str(data["word"])
	word = word.split(" ")
	word = word[0]
	if "North" in word[0:5]:
		return 1
	elif "north" in word[0:5]:
		return 1
	elif "South" in word[0:5]:
		return 1
	elif "south" in word[0:5]:
		return 1
	elif "East" in word[0:4]:
		return 1
	elif "east" in word[0:4]:
		return 1
	elif "West" in word[0:4]:
		return 1
	elif "west" in word[0:4]:
		return 1
	return 0

def followedByOrPrecededByTo(data):
	prevword = str(data["prev4"])
	nextword = str(data["after0"])
	if (prevword == "to") :
		return 1
	elif (nextword == "to") :
		return 1
	return 0

def dictionaryTwoLetterCapitalWordexceptUSUKEU(data):
	word = str(data["word"])
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
			elif (word == "MP") :
				return 0
			elif (word == "UP") :
				return 0
			elif (word == "SA") :
				return 0
			else :
				return 1
	return 0	
'''
f = open('../data/data_window_ngram-5.pkl', 'rb')
data = pd.read_pickle(f)
f.close()
#print(data.iloc[0])
#print("%20s | %20s  | %20s | %5s | %3s" %("previous word", "word", "next word", "label", "file_ids"))
print("%20s | %5s | %3s" %("word", "label", "file_ids"))
for index, row in data.iterrows():
	if(dictionaryTwoLetterCapitalWordexceptUSUKEU(row)):
		#print("%20s | %20s  | %20s | %5s | %3d" %(row["prev4"], row["word"], row["after0"], row["labels"], row["file_ids"]))
		print("%20s | %5s | %3d" %(row["word"], row["labels"], row["file_ids"]))
'''