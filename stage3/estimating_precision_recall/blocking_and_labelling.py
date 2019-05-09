import numpy as np
from IPython.core import debugger
from IPython.display import clear_output
breakpoint = debugger.set_trace
from google.colab import files

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', -1)
#!rm L.csv

Ci_filename = "Ci"

densityFlag = 0
i = 0
Ci = dfc.copy(deep=True)
n_rows = dfc.shape[0]
# L = pd.read_csv("L.csv")
L = pd.DataFrame()
i = L.shape[0]

print(dfc.shape[0])

## Run blocking step
Ci.drop_duplicates(inplace=True)

## Check number of authors (Blocking Rule)
for index, row in Ci.iterrows():
  a_id = row['A_id']
  b_id = row['B_id']
  a_entry = dfa.loc[ dfa['_id'] == a_id ]
  b_entry = dfb.loc[ dfb['_id'] == b_id ]
  a_authors = a_entry['Authors'].str.count(' and ')
  b_authors = b_entry['Authors'].str.count(',')
  a_n_authors = a_authors.values[0] + 1
  b_n_authors = b_authors.values[0] + 1
  
  
  if( a_n_authors != b_n_authors ):
    Ci.drop(index, inplace=True)
    
print(Ci.shape[0])

Ci.to_csv(Ci_filename)

B = Ci.copy(deep=True)

B['label'] = pd.Series(np.zeros(B.shape[0],).astype(int), index = B.index )



for index, row in B.iterrows():
  print("Curr Iteration: {}".format(i))
  a_id = row['A_id']
  b_id = row['B_id']
  
  a_entry = dfa.loc[ dfa['_id'] == a_id ]
  b_entry = dfb.loc[ dfb['_id'] == b_id ]
  
  display(a_entry)
  display(b_entry)

  l = raw_input()

  B.loc[index]['label'] = l

  if(i % 10 == 0):
    B.to_csv("B.csv")
  if(i % 50 == 0):
    files.download("B.csv")
    
#     break
    
  clear_output()
  i = i+1
  

n_labeled = B.shape[0] 
n_pos = B["label"].sum()
n_neg = n_labeled - n_pos

d = float(n_pos) / float(n_labeled)
print("Curr density: {} \n".format(d))