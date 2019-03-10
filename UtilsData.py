#### Standard Library Imports
import re
#### Library Imports
from IPython.core import debugger
breakpoint = debugger.set_trace
import numpy as np
import pandas as pd



def GetWordsFromTextFile(text_file):
    ''' GetWordsFromTextFile
            Performs the necessary pre-processing of text to return a clean list of words.
    '''
    text = text_file.read()
    text = text.strip() # Remove all beginning and end whitespace and new line characters
    text = text.replace('\n', ' ') # Replace new line characters with whitespace so the window can easily look across sentences 
    text = text.replace('-', ' ') # For special cases like US-China we should just remove the -. 
    text = text.replace('—', ' ') # For special cases like US-China we should just remove the -. 
    text = text.replace('/', ' ') # For special cases like US/China we should just remove the /. 
    text = re.sub(' +', ' ', text) # Remove all duplicate whitespace characters
    ## After splitting at ' ' we should not get any individual word to be only whitespace. Instead they would be empty strings.
    words = text.split(' ') 
    return words

def RemoveLocTags(word_arr):
    for i in range(len(word_arr)):
        word_arr[i] = word_arr[i].replace("<loc>","")
        word_arr[i] = word_arr[i].replace("</loc>","")
    return word_arr 


def DocumentToDataFrame(file_path, window_size = 1, ngram = 0, ID = -1):
    ''' DocumentToDataFrame
            Read document and produces an dataframe that contains the data and the labels
    '''
    text_file = open(file_path)
    ## Get list of all words with the appropriate preprocessing
    words = GetWordsFromTextFile(text_file)
    n_words = len(words)
    ## Initialize data structures and helper variables
    col_names_data = ["w" + str(i) for i in range(window_size)]
    col_names_ngram_prev = ["prev" + str(i) for i in range(ngram)] 
    col_names_ngram_after = ["after" + str(i) for i in range(ngram)] 
    data_window = pd.DataFrame(columns=col_names_data)
    data_ngram_prev = pd.DataFrame(columns=col_names_ngram_prev)
    data_ngram_after = pd.DataFrame(columns=col_names_ngram_after)
    labels = pd.DataFrame(columns=['labels'])
    file_ids = pd.DataFrame(columns=['file_ids'])
    curr_row = 0
    n_locations = 0
    is_location = False
    ## Process each window (stride=1) 
    for i in range(n_words - window_size + 1):
        st_idx = i
        end_idx = i + window_size
        curr_window = words[st_idx:end_idx]
        curr_label = False
        curr_ngram_prev = ['<N/A>']*ngram
        curr_ngram_after = ['<N/A>']*ngram
        ## Store ngrams. Deal with beginning and ending corner cases
        if(i < ngram):
            curr_ngram_prev[ngram-i:] = words[0:i]
        else:
            curr_ngram_prev = words[i-ngram:i]
        if(i+window_size+ngram > n_words):
            curr_ngram_after[0:n_words-i-window_size] = words[i+window_size:]
        else:
            curr_ngram_after = words[i+window_size:i+window_size+ngram]
        ## If curr_window contains empty string take a look at it.
        if( '' in curr_window ):
            print("ERROR: Curr window has empty String!!!!!!!!!!")
            breakpoint()
            continue
        ## If first word has <loc> then see if full string is a 
        if( ('<loc>' in curr_window[0]) and ('</loc>' in curr_window[-1]) ):
            n_open_tags = 0
            curr_label = True
            for j in range(len(curr_window)):
                n_open_tags = n_open_tags + curr_window[j].count("<loc>")
                n_open_tags = n_open_tags - curr_window[j].count("</loc>")
                if((n_open_tags <= 0) and (j != window_size - 1)):
                    curr_label = False
                    break
        # ##
        curr_window = RemoveLocTags(curr_window)
        curr_ngram_prev = RemoveLocTags(curr_ngram_prev)
        curr_ngram_after = RemoveLocTags(curr_ngram_after)

        # for j in range(window_size):
        #     w = curr_window[j]
        #     if(('<loc>' in w) and ('</loc>' in w) ):
        #         is_location = True
        #     elif('<loc>' in w): 
        #         n_locations = n_locations + 1
        #         is_location = True
        #     elif('</loc>' in w): 
        #         n_locations = n_locations - 1
        #         is_location = True        
        #     curr_labels[j] = is_location
        #     is_location = (n_locations > 0)
        
        data_window.loc[curr_row] = curr_window
        data_ngram_prev.loc[curr_row] = curr_ngram_prev
        data_ngram_after.loc[curr_row] = curr_ngram_after
        labels.loc[curr_row] = curr_label
        file_ids.loc[curr_row] = ID
        curr_row = curr_row + 1
    # breakpoint()
    ## Return single dataframe that contains the data in the first $window_size$ columns and the file_ids in the rest of file_ids columns
    return pd.concat([data_window,data_ngram_prev,data_ngram_after,labels,file_ids],axis=1)

