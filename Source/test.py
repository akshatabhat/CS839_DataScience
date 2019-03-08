import pickle
import pandas as pd

f = open('../data/data_window-1_ngram-5.pkl', 'rb')
data1 = pd.read_pickle(f)
f.close()
data1["word"] = data1["w0"]
pd.concat([data1, data1["word"]], axis=1, ignore_index=True)
data1.drop(["w0"], axis=1, inplace=True) 

f = open('../data/data_window-2_ngram-5.pkl', 'rb')
data2 = pd.read_pickle(f)
f.close()
data2["word"] = data2["w0"] + " " + data2["w1"]
pd.concat([data2, data2["word"]], axis=1, ignore_index=True)
data2.drop(["w0", "w1"], axis=1, inplace=True) 

f = open('../data/data_window-3_ngram-5.pkl', 'rb')
data3 = pd.read_pickle(f)
f.close()
data3["word"] = data3["w0"] + " " + data3["w1"] + " " + data3["w2"]
pd.concat([data3, data3["word"]], axis=1, ignore_index=True)
data3.drop(["w0", "w1", "w2"], axis=1, inplace=True) 