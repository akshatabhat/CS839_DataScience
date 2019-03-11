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
	return 0
'''
f = open('../data/data_window_ngram-5.pkl', 'rb')
data = pd.read_pickle(f)
f.close()
#print(data.iloc[0])
#print("%20s | %20s  | %20s | %5s | %3s" %("previous word", "word", "next word", "label", "file_ids"))
print("%20s | %5s | %3s" %("word", "label", "file_ids"))
for index, row in data.iterrows():
	if(dictionaryTwoLetterCapitalWordexceptUSUKEU(data.iloc[index])):
		#print("%20s | %20s  | %20s | %5s | %3d" %(row["prev4"], row["word"], row["after0"], row["labels"], row["file_ids"]))
		print("%20s | %5s | %3d" %(row["word"], row["labels"], row["file_ids"]))
'''