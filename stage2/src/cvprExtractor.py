from lxml import html
import requests
import pandas as pd
import numpy as np
import time
from IPython.core import debugger
breakpoint = debugger.set_trace

##Can you do the following attributes for each paper in the CVPR page :
# 1. Tag (the bibtex tag used like Das_2018_CVPR)
# 2. Authors
# 3. Title
# 4. Month
# 5. Year

# Note: For some reason the 2013 cvpr page contains ICCV 2013 workshop papers instead of cvpr so we dont add it here. 
cvpr_years = ['2014','2015', '2016', '2017', '2018']
# cvpr_years = ['2018']

webpage_prefix = 'http://openaccess.thecvf.com/'
df = pd.DataFrame(columns=['Tag','Title', 'Authors','Month', 'Year', 'JournalRef', 'Abstract'])
total_paper_count = 0


for year in cvpr_years:

    webpage_name = 'CVPR' + year + '.py'
    page = requests.get(webpage_prefix + webpage_name)
    tree = html.fromstring(page.content)

    papers_data = tree.xpath('//div[@class="bibref"]/text()')
    n_papers = int(len(papers_data) / 7)
    for i in range(n_papers):
        st_idx = i*7
        end_idx = st_idx + 7
        curr_paper_data = papers_data[st_idx:end_idx]
        print("Start: {}, End: {}".format(st_idx,end_idx))
        # Tag starts at character in index 16, ends at the second to last character
        tag_data = curr_paper_data[0] 
        tag = tag_data[16:-1]
        # Authour list starts at character in index 11, ends at the third to last character
        authors_data = curr_paper_data[1]
        authors = authors_data[11:-2]
        # Title starts at character in index 10, ends at the third to last character
        title_data = curr_paper_data[2]
        title = title_data[10:-2]
        # monh (conference title) starts at character in index 10, ends at the third to last character
        month_data = curr_paper_data[4]
        month = month_data[10:-2]
        # Year (conference title) starts at character in index 9, ends at the second to last character
        year_data = curr_paper_data[5]
        year = year_data[9:-1]

        ## Get current paper link to page
        paper_href = tree.xpath('//*[@id="content"]/dl/dt[{}]/a/@href'.format(i+1))
        paper_link = webpage_prefix + paper_href[0]
        journal = ''
        abstract = ''
        ## Extract journal ref and abstract from paper's webpage
        curr_page = requests.get(paper_link)
        curr_tree = html.fromstring(curr_page.content)
        ## a few papers have a broken link to their webpage
        if(curr_page.ok):
            # Journal        
            journalref_data = curr_tree.xpath('//*[@id="authors"]/text()')[1]
            journalref = journalref_data[2:-1] ## skip empty and newline characters
            # Abstract        
            abstract_data = curr_tree.xpath('//*[@id="abstract"]/text()')[0]
            abstract = abstract_data[1:] # skip first character which is \n
        else:
            breakpoint()
        ## Add row to data framce
        row_data = [tag,title,authors,month,year, journalref, abstract]
        df.loc[total_paper_count + i] = row_data

        if( i % 25 == 0): 
            print('Tag: {}\n Title: {}\n Authors: {}\n Month: {}\n Year: {}\n Journalref: {}\n Abstract: {}\n'.format(tag,title,authors,month,year, journalref, abstract[0:10]))
            time.sleep(2)
    total_paper_count = total_paper_count + n_papers
    

df.to_csv('data/cvpr.csv', index=False)