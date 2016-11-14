import json
import urllib

x = ('http://python-data.dr-chuck.net/comments_42.json')
print 'Retrieving', x
url = urllib.urlopen(x)
data = url.read()
print 'Retrieved',len(data),'characters'
print data
info = json.loads(data)
print 'User count:', len(info)

for item in info:
    print item["comments"],["name"]


