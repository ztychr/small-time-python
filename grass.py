import math
import sys
import fileinput

lists = []
sprinklers = 0
length = 0
width = 0
counter = 0

for line in fileinput.input():
    stream = line.split()
	
    if len(stream) == 3:
		sprinklers = stream[0]
		length = stream[1] 
		width = stream[2]

    elif len(stream) == 2:
		data = stream[0:2]
		lists.append(data)

def getC(a, b):
	rt = a*a+b*b
	c = math.sqrt(rt)
	return c

def getB(a, c):
	b = math.sqrt(c*c-a*a)
	return b


for i in lists:
	sideC = lists[counter][1]
	b = getB(float(width)/float(2), float(sideC))
	start = float(lists[counter][0])-b
	stop = float(lists[counter][0])+b
	print counter,". ",start," - ",stop
	counter+=1

