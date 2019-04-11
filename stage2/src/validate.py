import pandas as pd

arxiv_df = pd.read_csv('./data/arxiv.csv')

cvpr_df = pd.read_csv('./data/cvpr.csv')
print(arxiv_df.loc(1))

mergedStuff = pd.merge(arxiv_df, cvpr_df, on=['Title'])
print(mergedStuff)