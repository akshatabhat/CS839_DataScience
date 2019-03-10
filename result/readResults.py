import pandas as pd

f = open("Random Forest_false_pos.pkl",'rb')
data = pd.read_pickle(f)
for index, row in data.iterrows():
	print("%s %s" %(row["file_ids"], row["word"]))