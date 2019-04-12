from lxml import html
import requests
import pandas as pd
import numpy as np
page = requests.get('https://arxiv.org/search/advanced?advanced=&terms-0-term=cs.cv&terms-0-operator=AND&terms-0-field=all&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=date_range&date-year=&date-from_date=2011&date-to_date=2018&date-date_type=submitted_date&abstracts=show&size=200&order=-announced_date_first')
tree = html.fromstring(page.content)

results_per_page = 200
total_pages = 50 #int(tree.xpath('/html/body/main/div[1]/div[1]/h1/text()')[0].replace('\n','').strip().split('of')[1].strip().split(' ')[0].replace(',',''))//results_per_page
df = pd.DataFrame(columns=['Tag','Title', 'Authors','Month', 'Year', 'Abstract', 'JournalRef'])
for i in range(0, total_pages):
	for j in range(1, results_per_page+1):
		tag = tree.xpath('/html/body/main/div[2]/ol/li['+str(j)+']/div/p/a/text()')[0]
		title = tree.xpath('/html/body/main/div[2]/ol/li['+str(j)+']/p[@class="title is-5 mathjax"]/text()')[0].replace('\n','').strip()
		authors = ', '.join(tree.xpath('/html/body/main/div[2]/ol/li['+str(j)+']/p[@class="authors"]/a/text()'))
		submitted = tree.xpath('/html/body/main/div[2]/ol/li['+str(j)+']/p[@class="is-size-7"]/text()')[0].replace(';','').replace('\n','').strip().split(',')
		month = submitted[0].split(' ')[1]
		year = submitted[1]
		abstract = tree.xpath('/html/body/main/div[2]/ol/li['+str(j)+']/p[@class="abstract mathjax"]/span[@class="abstract-full has-text-grey-dark mathjax"]/text()')[0].strip()
		check_journal_ref = tree.xpath('/html/body/main/div[2]/ol/li['+str(j)+']/p[@class="comments is-size-7"]/span[@class="has-text-black-bis has-text-weight-semibold"]/text()')
		if 'Journal ref:' in check_journal_ref:
			journal_ref = tree.xpath('/html/body/main/div[2]/ol/li['+str(j)+']/p[@class="comments is-size-7"]/text()[last()]')[-1].strip()
		else:
			journal_ref = "NA"
		df.loc[i*results_per_page+j] = [tag, title, authors, month, year, abstract, journal_ref]
	nextpage = tree.xpath('/html/body/main/div/nav/a[@class="pagination-next"]/@href')
	page = requests.get("https://arxiv.org" + nextpage[0])
	tree = html.fromstring(page.content)
#print(df)

df.to_csv('./../data/arxiv.csv', index=False)