'''
Created on Jul 28, 2016

@author: lucas
'''

from lxml import html
import requests
import re
import pickle
import sys

BASE_URL = 'http://www.pagina12.com.ar'

def writeList(urlList):
    '''
    Write pagina12_urls.txt file with the urls used
    and a pickle object
    '''

    pickle.dump(modifiedUrls, open("lista.p", "wb"))

    file = open("pagina12_urls.txt", "w")

    for element in urlList:
        file.write(element + '\n')

    file.close()


if __name__ == '__main__':

    page = requests.get('http://www.pagina12.com.ar')
    print(page)

    try:
        compiledRe = re.compile(r'href=[\'"]?([^\'">]+/2-\d{6}-\d{4}-\d{2}-\d{2}[^\'">]+)')
        hrefMatches = compiledRe.findall(str(page.content))
        print(hrefMatches)
    except Exception as error:
        print(error)
        sys.exit()

    '''Set of urls without duplications'''
    modifiedUrls = {(BASE_URL + url) for url in hrefMatches}
    '''write in pickle and file to persist them'''
    writeList(modifiedUrls)

    count = 0

    for url in modifiedUrls:
        try:
            page = requests.get(url)
            tree = html.fromstring(page.content)
        except Exception as error:
            print(error)
            continue
        nota = tree.xpath('//div[@id="cuerpo"]//p/text()')
        file = open(str(count)+".txt", "w")
        for parrafo in nota:
            file.write(parrafo)
        file.close()
        count +=1

    sys.exit()
