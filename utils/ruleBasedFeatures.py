import pandas as pd
import nltk
from IPython.core import debugger
breakpoint = debugger.set_trace



def prevWordIsThe(row):
    return 'the' in str(row['prev4']).lower() 


def prevStrIsInThe(row):
    prev_str = str(row['prev3']) + ' ' + str(row['prev4'])
    return 'in the' in prev_str.lower() 

def wordContainsDayOfWeek(row):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    word = str(row['word']).lower()
    for day in days:
        if(day in word):
            return True
    return False
        
def wordContainsMonth(row):
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    word = str(row['word']).lower()
    for month in months:
        if(month in word):
            return True
    return False


# df = pd.read_pickle('../Data/data_window_ngram-5.pkl')

# row = df.iloc[0]
# print(row)

# pos_counts = posCounts(row)
# print(pos_counts)
# pos_counts_ngram = posCountsNGram(row, ngram=6)
# print(pos_counts_ngram)

