import pandas as pd

arxiv_df = pd.read_csv('../data/arxiv.csv')

cvpr_df = pd.read_csv('../data/cvpr.csv')

count = 0
#only for true matches
	#print(index1, row1['Title'])
for index2, row2 in cvpr_df.iterrows():
	for index1, row1 in arxiv_df.iterrows():
		arxiv_title = row1['Title'].strip()
		cvpr_title = row2['Title'].strip()
		if (arxiv_title == cvpr_title):
			print("arxiv index: %d cvpr index: %d Title: %s" %(index1, index2, arxiv_title))
			count += 1

print("Total matches : %d" %count)