# Crawler

# Requests

Request for website

Get response separately of get and post as follow:
```python=
response = requests.get("{url}")
response = requests.post("{url}")
```

response to text as follow:
```python=
response.content
# or
response.text
```



# lxml
lxml is xml of parser.
When get the xml format of content that can use to xpath analysis xml then get data that you want.

For example:
```=python
tree = etree.HTML({html content})
xpath = tree.xpath('//div[@class="{value}"]/a')

xpath.get('href') # get href
xpath.text # get text content

```

// = root
[@{title}={value}]


# Seleium
The function mainly simulate the browser then crawl website one of tool.

First download the browser driver.
[google driver](https://chromedriver.chromium.org/downloads)

Requirement library
```
selenium
```

Call the library then use the driver
```python=
from selenium import webdriver
driver = webdriver.Chrome("{driver path}")
```

