import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))

print 'Retrieving: ',url

def engine(url,pos,count):
    x=0
    while x<count:
        c=0
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        for tag in tags:
            c+=1
            if c == pos:
                url = tag.get('href', None)
                print 'Retrieving: ',url
                x+=1
                
engine(url,pos,count)
