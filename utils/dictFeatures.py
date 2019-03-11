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
	return 0	