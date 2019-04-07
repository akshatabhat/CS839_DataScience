from lxml import html
import requests

page = requests.get('https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=cs.cv&terms-0-field=all&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date=2011&date-to_date=2018&date-date_type=submitted_date&abstracts=show&size=50&order=-announced_date_first')
tree = html.fromstring(page.content)

title = tree.xpath('/html/body/main/div[2]/ol/li/p[@class="title is-5 mathjax"]/text()')
authors = tree.xpath('/html/body/main/div[2]/ol/li/p[@class="authors"]/text()')
submitted = tree.xpath('/html/body/main/div[2]/ol/li/p[@class="is-size-7"]/text()')
#print(title)
nextpage = tree.xpath('/html/body/main/div/nav/a[@class="pagination-next"]/@href')
#print(nextpage[0])
page = requests.get("https://arxiv.org" + nextpage[0])
tree = html.fromstring(page.content)
title += tree.xpath('/html/body/main/div[2]/ol/li/p[@class="title is-5 mathjax"]/text()')
authors += tree.xpath('/html/body/main/div[2]/ol/li/p[@class="authors"]/text()')
submitted += tree.xpath('/html/body/main/div[2]/ol/li/p[@class="is-size-7"]/text()')
print(title)