import re

fh = open("regex_sum_362931.txt")
sum = 0
for line in fh:
  line = line.rstrip()
  x = re.findall('[0-9]+',line)
  for y in x:
    sum = sum + int(y)

print sum
