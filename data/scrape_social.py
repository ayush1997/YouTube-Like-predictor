# To run:
# pip install asynchronizer lxml requests

import requests
# using lxml tree to keep the example short
from lxml import html
from asynchronizer import asynchronize, Wait, setWorkers,a



filename = "channelIdList"
fileObject = open(filename,'r')
urls = pickle.load(fileObject)


# to set custom number of threads
setWorkers(64)
session = requests.Session()
requests_made = 0
total_requests = 0


@asynchronize
def extract(url):
    global requests_made,total_requests


    url = "https://www.youtube.com/channel/"+url+"/about"
    page = requests.get(url)
    tree = html.fromstring(page.content)

    social_links = tree.xpath("//div[@class='about-metadata branded-page-box-padding clearfix ']/ul/li/a/@href")
    length =  len(social_links)
    print length

for url in urls:
    extract(url)
    total_requests += 1

Wait()
