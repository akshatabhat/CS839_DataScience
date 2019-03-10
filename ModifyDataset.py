#### Standard Library Imports
import re
import os
#### Library Imports
from IPython.core import debugger
breakpoint = debugger.set_trace
import numpy as np
import scipy
import pandas as pd
import matplotlib
#### Local Imports
import UtilsData

window_sizes = [1,2]

for window_size in window_sizes:
    #### Paths and filenames
    in_path = "./FileRepo_Annotated/"
    out_path = "./Data/"
    out_filename = "data"
    #### Files to parse. 
    ## Files that are currently annotated: 1-110, 200-310, 400-510.
    file_ids = [485]
    #### Parsing parameters
    ## Number of words that we look at one time.
    # window_size = 1
    ngram = 5

    df = pd.DataFrame()
    #### Parse single file
    for i in file_ids:
        in_filename = str(i) + ".txt"
        in_file_path = in_path+in_filename
        ## Check that file exists. Some files were renamed or remove during annotation
        if(os.path.isfile(in_file_path)):
            print("Processing {} ... ".format(in_file_path))
            curr_df = UtilsData.DocumentToDataFrame(file_path=in_file_path, window_size=window_size, ngram=ngram, ID = i)
        else:
            print("********* File {} does not exist *********".format(in_file_path))
            continue
        ## Append to dataframe
        df = pd.concat([df,curr_df],axis=0)

    out_filename_info = "_window-" + str(window_size) + "_ngram-" + str(ngram)

    ## Load previous dataframe and remove all entries
    df_prev = pd.read_pickle(out_path + out_filename + out_filename_info + ".pkl")
    for ID in file_ids:
        df_prev = df_prev[df_prev.file_ids != ID]
    ## Add entries for dataframes that were redone
    df_prev = pd.concat([df_prev,df],axis=0)

    df_prev.to_pickle(out_path + out_filename + out_filename_info + ".pkl")

