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
    'hi',
    'javascript',
    'mongodb',
]

jsFileSave = 'json_file.js'
rssUrl = "https://habrahabr.ru/rss/hub"

xml_content = ''

file = open(jsFileSave, 'w')
file.write(';var json_file = (function(){ return [')

filter_query = input("Выбрать: Лучшее (/best) Лучшее за все время (best/alltime) или по умолчанию свежие: ")

if (filter_query == ''): 
   filter_query = '/'

if (file):

    result = True

    for hubName in listHub:

        json_block = ' { "name" : "' + hubName + '", "data" : '

        fullUrl = rssUrl + '/' + hubName + '' + filter_query

        print('Получаем ' + fullUrl);

        try:
            response = requests.get(fullUrl, verify=False)
        except Exception:
            print('Не удалось получить...')
            result = False
            break

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

print('Записали в файл ' + jsFileSave)

if (result):
    shutil.move('json_file.js', '../frontend/src/json_file.js')
    print('Переносим файл в ../src/' + jsFileSave)
else:
    print('При получении данных возникли проблемы...');


#print(';var json_file = (function(){ return ' + json_content + ';})();')
