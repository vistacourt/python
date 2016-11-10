import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
l=[]
x=0
soup = BeautifulSoup(html)
tags = soup('span')
for tag in tags:
    x+=1
    l.append(int(tag.contents[0]))
    y=sum(l)
print 'Count ',x
print 'Sum ',y

