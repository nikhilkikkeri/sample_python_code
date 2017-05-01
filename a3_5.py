import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url
html = urllib.urlopen(url).read()
print 'Retrieved',len(html),'characters'
print html
tree = ET.fromstring(html)
results = tree.findall('comments/comment')
print 'Count=',len(results)
sum=0
for item in results:
  sum = sum + int(item.find('count').text)

print sum
