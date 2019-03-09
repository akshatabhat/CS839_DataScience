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
    breakpoint()
    for (word, tag) in tagged_words:
        pos_counts[tag] = pos_counts[tag] + 1
    
    return list(pos_counts.values())


def posCountsNGram(data, ngram=1):
    prev_pos_counts = {'CC': 0,'CD': 0,'DT': 0,	'EX': 0,'FW': 0,'IN': 0,'JJ': 0,'JJR': 0,'JJS': 0,'LS': 0,'MD': 0,'NN': 0,'NNS': 0,'NNP': 0,'NNPS': 0,'PDT': 0,'POS': 0,	'PRP': 0,	'PRP$': 0,	'RB': 0,	'RBR': 0,	'RBS': 0,	'RP': 0,	'TO': 0,	'UH': 0,	'VB': 0,	'VBD': 0,	'VBG': 0,	'VBN': 0,	'VBP': 0,	'VBZ': 0,	'WDT': 0,	'WP': 0,	'WP$': 0,	'WRB': 0 }
    after_pos_counts = {'CC': 0,'CD': 0,'DT': 0,	'EX': 0,'FW': 0,'IN': 0,'JJ': 0,'JJR': 0,'JJS': 0,'LS': 0,'MD': 0,'NN': 0,'NNS': 0,'NNP': 0,'NNPS': 0,'PDT': 0,'POS': 0,	'PRP': 0,	'PRP$': 0,	'RB': 0,	'RBR': 0,	'RBS': 0,	'RP': 0,	'TO': 0,	'UH': 0,	'VB': 0,	'VBD': 0,	'VBG': 0,	'VBN': 0,	'VBP': 0,	'VBZ': 0,	'WDT': 0,	'WP': 0,	'WP$': 0,	'WRB': 0 }
    ## construct ngram
    prev_ngram_str = ""
    after_ngram_str = ""
    for i in range(ngram):
        if(str(data["prev" + str(i)]) == '<N/A>'):  
            prev_ngram_str = prev_ngram_str + " N/A"
        else:  
            prev_ngram_str = prev_ngram_str + " " + str(data["prev" + str(i)])
        if(str(data["after" + str(i)]) == '<N/A>'):  
            after_ngram_str = after_ngram_str + " N/A"
        else:  
            after_ngram_str = after_ngram_str + " " + str(data["after" + str(i)])
    prev_ngram_tokens = nltk.word_tokenize(prev_ngram_str) 
    after_ngram_tokens = nltk.word_tokenize(after_ngram_str) 
    prev_ngram_tags = nltk.pos_tag(prev_ngram_tokens) 
    after_ngram_tags = nltk.pos_tag(after_ngram_tokens) 
    for (word, tag) in prev_ngram_tags:
        prev_pos_counts[tag] = prev_pos_counts[tag] + 1
    for (word, tag) in after_ngram_tags:
        after_pos_counts[tag] = after_pos_counts[tag] + 1

    return list(prev_pos_counts.values()) + list(after_pos_counts.values())


# df = pd.read_pickle('../Data/data_window_ngram-5.pkl')

# row = df.iloc[0]
# print(row)

# pos_counts = posCounts(row)
# print(pos_counts)
# pos_counts_ngram = posCountsNGram(row, ngram=6)
# print(pos_counts_ngram)

