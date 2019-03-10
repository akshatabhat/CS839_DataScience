import pandas as pd

f = open("Random Forest_false_pos.pkl",'rb')
data = pd.read_pickle(f)
for index, row in data.iterrows():
	print("%4s | %30s | %30s | %30s" %(row["file_ids"], row["prev4"], row["word"], row["after0"]))
f.close()

f = open("Random Forest_false_pos_train.pkl",'rb')
data = pd.read_pickle(f)
for index, row in data.iterrows():
	print("%4s | %30s | %30s | %30s" %(row["file_ids"], row["prev4"], row["word"], row["after0"]))
f.close()