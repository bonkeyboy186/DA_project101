import scrapy
import requests
from scrapy.utils import response
from bs4 import BeautifulSoup


class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://192.168.17.84/freebix']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
    def scarface(self):
    # To recurse next page
        response = requests.get('http://brickset.com/sets/2019')

        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')

        urls = [img['src'] for img in img_tags]

        for url in urls:
            filename = requests.search(r'/([\w_-]+[.](jpg))$', url)
            if not filename:
                print("Did not match with the url: {}".format(url))
                continue
            with open(filename.group(1), 'wb') as f:
                if 'http' not in url:
                    # sometimes an image source can be relative
                    # if it is provide the base url which also happens
                    # to be the url variable atms.
                    url = '{}{}'.format('http://192.168.17.84/freebix', url)
                response = requests.get(url)
                f.write(response.content)
