import pandas as pd
import nltk
# from IPython.core import debugger
# breakpoint = debugger.set_trace

#import pickle

def posCounts(data):
    pos_counts = {
        'CC': 0,
        'CD': 0,
        'DT': 0,	
        'EX': 0,	
        'FW': 0,	
        'IN': 0,	
        'JJ': 0,	
        'JJR': 0,	
        'JJS': 0,	
        'LS': 0,	
        'MD': 0,	
        'NN': 0,	
        'NNS': 0,	
        'NNP': 0,	
        'NNPS': 0,
        'PDT': 0,	
        'POS': 0,	
        'PRP': 0,	
        'PRP$': 0,	
        'RB': 0,	
        'RBR': 0,	
        'RBS': 0,	
        'RP': 0,	
        'TO': 0,	
        'UH': 0,	
        'VB': 0,	
        'VBD': 0,	
        'VBG': 0,	
        'VBN': 0,	
        'VBP': 0,	
        'VBZ': 0,	
        'WDT': 0,	
        'WP': 0,	
        'WP$': 0,	
        'WRB': 0 }	
    words = str(data["word"])
    tokens = nltk.word_tokenize(words)
    tagged_words = nltk.pos_tag(tokens)
    for (word, tag) in tagged_words:
        pos_counts[tag] = pos_counts[tag] + 1
    return list(pos_counts.values())


# df = pd.read_pickle('../Data/data_window_ngram-5.pkl')

# row = df.iloc[552328]
# print(row)

# posCounts = posCounts(row)
# print(posCounts)

