import json
import urllib

url = raw_input('Enter location: ')
print 'Retrieving ',url
html = urllib.urlopen(url).read()
print 'Retrieved ',len(html),' characters'

info = json.loads(html)
sum = 0
for item in info['comments']:
  for k,v in item.items():
    if k == 'count':
      sum = sum + v

print sum

  
