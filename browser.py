# Use the request library
from lxml import html
import requests
# Set the target webpages
url = 'http://brickset.com/sets/2019'
r = requests.get(url)
# This will get the full page
print(r.text)
# This will get the status code
print("Status code:")
print("\t *", r.status_code)
# This will just get just the headers
h = requests.head(url)
print("Header:")
print("********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("********")

# This will modify the headers user-agent
headers = {
    'User-Agent': 'Iphone 8'
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)

# Display the Website header

response = requests.get(url)
headers = response.headers
html = response.text
print(html)

# Modify the Header user-agent to display "Mobile"

headers = {
    'user-agent' : 'Mobile'
}

page = requests.get('http://brickset.com/sets/2019/', headers=headers)
tree = html.fromstring(page.content)

userAgent = tree.xpath('//*[@id="uas_textfield"]/text()')
print(userAgent[0])


