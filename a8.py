fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    tmp = line.split()
    for aword in tmp:
        if not aword in lst:
            lst.append(aword)
print(lst)
