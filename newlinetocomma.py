source = open('/Users/Matthew/Desktop/in.txt','r')

destination = open('/Users/Matthew/Desktop/out.txt','r+')

myArray = []

for line in source:
	myArray.append(line)

destination.read()
print destination.read()
for line in destination:
	print line

newlist = []
for w in myArray:
	if w[4]=='|':
		newlist.append(w[0:4])

list(enumerate(myArray))

print newlist

for e in newlist:
	destination.write("'"+e+"',")

