# -*- coding=utf-8 -*-

import requests
from lxml import etree

root_url = 'https://udn.com/'
url = "https://udn.com/news/breaknews/{page}"

# get html object
response = requests.request("GET", url.format(page=1))

# get html content
content = response.content

# Convert to xml parse object 
xtree = etree.HTML(content)

# analysis the xml  using the xpath
target_sub_news = xtree.xpath('//div[@id="breaknews_body"]/dl/dt/h2/a')

for _obj in target_sub_news:
	print("url = ",root_url+_obj.get('href'))
	print("title = ",_obj.text)

	# get sub content   drill down
	sub_response = requests.request("GET", root_url+_obj.get('href'))
	sub_content = sub_response.content
	sub_xtree = etree.HTML(sub_content)
	target_sub_news = sub_xtree.xpath('//div[@id="article_body"]/p//text()')

	print("news content = ", '\n'.join(target_sub_news))

	# stop loop
	exit()