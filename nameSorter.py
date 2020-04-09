import sys

#get a list of names
names = [line.strip() for line in sys.stdin]

#sort the names
names.sort()
names.sort(key=len)

#print the names
for name in names:
    print(name)
