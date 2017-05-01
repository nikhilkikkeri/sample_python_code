# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

count = raw_input('Enter count:')
count = int(count)

position = raw_input('Enter position:')
position = int(position)
print 'Retrieving:', url

i=0
while i < count :
  idx = 0;
  # Retrieve all of the anchor tags
  tags = soup('a')
  while idx < position-1:
    idx = idx+1
  print 'Retrieving:', tags[idx].get('href', None)
  url = tags[idx].get('href', None)
  html = urllib.urlopen(url).read()
  soup = BeautifulSoup(html)
  i=i+1
