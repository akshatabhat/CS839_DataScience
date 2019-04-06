from lxml import html
import requests

page = requests.get('https://arxiv.org/search/?query=data+science&searchtype=all&source=header')
tree = html.fromstring(page.content)

authors = tree.xpath('//p[@class="title is-5 mathjax"]/text()')
print(authors)