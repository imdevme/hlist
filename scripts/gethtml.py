#!/usr/local/bin/python3

#http://thehtmldom.sourceforge.net/#install

import requests
from htmldom import htmldom
import os

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = ''

inputUrl = input("Введите URL: ")
inputQuery = input("Query: ")

if (inputUrl):
    url = inputUrl

scriptDir = os.path.dirname(__file__)

savePath = scriptDir + '/download.html'

if (not os.path.isfile(savePath) and url):
    try:
        response = requests.get(url, verify=False)
    except Exception:
        print('Не удалось получить...')

    if (response.status_code == 200):
        print ('Html получен')
        file = open(savePath, 'w')
        file.write(response.text)
        file.close()

with open(savePath, 'r') as content_file:
    content = content_file.read()

dom = htmldom.HtmlDom()
dom = dom.createDom(content)

query = '#post_333002 > .post_preview > .post__title > a'

if (inputQuery):
    query = inputQuery

postTitle = dom.find(query)

print(postTitle.text())
