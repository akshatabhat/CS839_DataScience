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
    text = re.sub(' +', ' ', text) # Remove all duplicate whitespace characters
    ## After splitting at ' ' we should not get any individual word to be only whitespace. Instead they would be empty strings.
    words = text.split(' ') 
    return words

def DocumentToDataFrame(file_path, window_size = 1):
    ''' DocumentToDataFrame
            Read document and produces an dataframe that contains the data and the labels
    '''
    text_file = open(file_path)
    ## Get list of all words with the appropriate preprocessing
    words = GetWordsFromTextFile(text_file)
    n_words = len(words)
    ## Initialize data structures and helper variables
    col_names = ["w" + str(i) for i in range(window_size)]
    data = pd.DataFrame(columns=col_names)
    labels = pd.DataFrame(columns=range(window_size))
    curr_row = 0
    n_locations = 0
    is_location = False
    ## Process each window (stride=1) 
    for i in range(n_words - window_size + 1):
        st_idx = i
        end_idx = i + window_size
        curr_window = words[st_idx:end_idx]
        curr_labels = [0]*window_size
        ## If curr_window contains empty string take a look at it.
        if( '' in curr_window ):
            print("ERROR: Curr window has empty String!!!!!!!!!!")
            breakpoint()
            continue
        for j in range(window_size):
            w = curr_window[j]
            if(('<loc>' in w) and ('</loc>' in w) ):
                is_location = True
            elif('<loc>' in w): 
                n_locations = n_locations + 1
                is_location = True
            elif('</loc>' in w): 
                n_locations = n_locations - 1
                is_location = True        
            curr_labels[j] = is_location
            is_location = (n_locations > 0)
        data.loc[curr_row] = curr_window
        labels.loc[curr_row] = curr_labels
        curr_row = curr_row + 1
    ## Return single dataframe that contains the data in the first $window_size$ columns and the labels in the rest of the columns
    return pd.concat([data,labels],axis=1)

