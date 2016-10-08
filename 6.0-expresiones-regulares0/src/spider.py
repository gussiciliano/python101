'''
Created on Jul 27, 2016

@author: zehemz
'''
from lxml import html
from lxml import etree
from io import StringIO, BytesIO
from copy import deepcopy
import requests
import re
import pickle

def writeList(list):
    file = open("websScrapeadas.txt", "wb")
    for element in list:
        file.write(element+ '\n')
    file.close()

BASE_URL = 'http://www.clarin.com'

page = requests.get('http://www.clarin.com')

try:

    compiledRe = re.compile(r'href=[\'"]?(.*_0_[^\'">]+)')
    matches = compiledRe.findall(page.content)
    print(matches)
except Exception as error:
    print(type(error))
    print(error)
    
modifiedUrls = [(BASE_URL + url) for url in matches]

pickle.dump(modifiedUrls, open("lista.p", "wb"))
writeList(modifiedUrls)
count = 0    
for url in modifiedUrls:
    try:
        page = requests.get(url)
    except Exception as error:
        print(error)
        continue
    try:
        tree = html.fromstring(page.content)
    except Exception as error:
        print(error)
        continue
    nota = tree.xpath('//div[@class="nota"]//p/text()')
    file = open(str(count)+".txt", "wb")
    for parrafo in nota:
        file.write(parrafo.encode("utf-8"))
    file.close()
    count +=1
    

