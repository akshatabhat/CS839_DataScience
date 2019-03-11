import pandas as pd

f = open("Random Forest_false_pos.pkl",'rb')
data = pd.read_pickle(f)
count = 0
for index, row in data.iterrows():
	#print("%4s | %30s | %30s | %30s" %(row["file_ids"], row["prev4"], row["word"], row["after0"]))
        if (len(row["word"]) == 2) :
            count += 1
            print(row["word"])
f.close()
print("Count = %d" %(count))
