import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
lst = tree.findall('.//count')
print 'Count: ',len(lst)
l=[]
for item in lst:
    l.append(int(item.text))
    total = sum(l)
print 'Sum :',total

