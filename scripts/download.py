#!/usr/local/bin/python3

import requests
import json
import xmltodict
import shutil
import time

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

listHub = [
    'programming',
    'funcprog',
    'oop',
    'complete_code',
    'refactoring',
    'webdev',
    'api',
    'hi'
]

rssUrl = "https://habrahabr.ru/rss/hub"

xml_content = ''

file = open('json_file.js', 'w')
file.write(';var json_file = (function(){ return [')

if(file):

    for hubName in listHub:

        json_block = ' { "name" : "' + hubName + '", "data" : '

        fullUrl = rssUrl + '/' + hubName + '/best/alltime/'

        response = requests.get(fullUrl, verify=False)

        print('Забираем: ' + fullUrl)

        if (response.status_code == 200):
            xml_content = response.text
            if (xml_content):
                parsed_xml = xmltodict.parse(xml_content)
                json_block += json.dumps(parsed_xml) + ' },'
                file.write(json_block)
                json_block = ''
                print('Пишем в файл...')

    time.sleep(2)


file.write(']; })();')
file.close()

shutil.move('json_file.js', '../src/json_file.js')

#print(';var json_file = (function(){ return ' + json_content + ';})();')
