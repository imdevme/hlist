#!/usr/local/bin/python3

import requests
import xml.etree.ElementTree as ET
import xml.dom.minidom
import os.path
import json
import xmltodict

xml_content = ''

if ( not os.path.isfile('download.xml')):
	response = requests.get("https://habrahabr.ru/rss/hub/mobile_dev/", verify=False)
	if (response.status_code == 200):
		xml_content = response.text
		file = open('donload.xml', 'w')
		if (xml_content):
			file.write(xml_content)
			file.close()



file = open('download.xml', 'r')
xml_string = file.read()
#dom = xml.dom.minidom.parse('donload.xml')
o = xmltodict.parse(xml_string)

#items = dom.getElementsByTagName("item")

# for item in items:
# 	title = item.getElementsByTagName('title')
# 	print(title)

print(';var json_file = (function(){ return ' + json.dumps(o) + ';})();')
