import pandas as pd
import pickle
import math

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
			elif (word == "SA") :
				return 0
			else :
				return 1
		else :
			return 0		
	elif (word[0:2].isupper() == True) :
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
	return 0	