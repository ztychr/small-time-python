import math
import sys
import fileinput

lists = []
sets = []

sprinklers = 0
length = 0
width = 0

def getB(a, c):
	b = math.sqrt(c*c-a*a)
	return b

def getC(a, b):
	rt = a*a+b*b
	c = math.sqrt(rt)
	return c

for line in fileinput.input():
	stream = line.split()

	if  int(sprinklers) > 2 and int(len(lists)) == int(sprinklers):
		print "SET: \n", sets, "\n"*3
		lists = []
		sets = []
		sprinklers = 0
		length = 0
		width = 0

	if len(stream) == 3:
		sprinklers = stream[0]
		length = stream[1]
		width = stream[2]

	elif len(stream) == 2:

		data = stream[0:2]
		lists.append(data)

		counter = 0
		sideC = lists[counter][1]
		b = getB(float(width)/float(2), float(sideC))
		pos = float(lists[counter][0])
		tmplist = [pos-b, pos+b]
		sets.append(tmplist)
		counter+=1

print sets


