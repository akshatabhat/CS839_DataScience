from lxml import html
import requests

page = requests.get('https://arxiv.org/search/?query=data+science&searchtype=all&source=header')
tree = html.fromstring(page.content)

title = tree.xpath('//p[@class="title is-5 mathjax"]/text()')
authors = tree.xpath('//p[@class="authors"]/text()')
submitted = tree.xpath('//p[@class="is-size-7"]/text()')
print(submitted)