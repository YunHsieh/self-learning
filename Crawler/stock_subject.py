# -*- coding:utf-8 -*-
import requests
from lxml import etree
import time
import json
from selenium import webdriver


url = "https://www.twse.com.tw/zh/listed/listingProfile"

category_content = ""
try:
	driver = webdriver.Chrome("chromedriver.exe")
	driver.get(url)
	driver.find_element_by_xpath("//form/a[@class='stock-code-browse']").click()
	time.sleep(5)
	category_content = driver.page_source
except:
	print(error)
finally:
	driver.close()

url = "https://www.twse.com.tw/zh/api/codeFilters?filter={num}"

xtree = etree.HTML(category_content)

target_content = xtree.xpath('//div[@class="group"]/div/a')
dict_stock = {i.get('data-val'):i.text for i in target_content}

stock_all_code = ["%.2d" % num for num in range(1,32,1)]


stock_detail = {}
for num in stock_all_code:
	response = requests.request("GET", url.format(num=num))
	content = {data.split('\t')[0]:data.split('\t')[1] for data in response.json()['resualt']}
	stock_detail[dict_stock[num]] = content
with open('resutl.json','w+', encoding='utf8') as _file:
	_file.write(json.dumps(stock_detail, indent=4, ensure_ascii=False))

exit()
