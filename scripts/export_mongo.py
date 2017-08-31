#!/usr/local/bin/python3

from pymongo import MongoClient

import sys
import pprint
import os
import json


def main(argv):

    pathToFile = input('Путь к файлу: ')
    pathToFile = os.path.realpath(pathToFile)

    with open(pathToFile) as json_file:
        json_data = json.load(json_file)

    pprint.pprint(json_data)

    print('Экспортируем в mongodb...')

    client = MongoClient('localhost', 27017)
    db = client.test
    articles = db.articles.find()

    if (articles.count()):
        print('Статьи:')
        for article in articles:
            pprint.pprint(article)


if (__name__ == '__main__'):
    # Если скрипт запущен как standalone то запускаем функцию main
    main(sys.argv[:1])
