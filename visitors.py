#gunzip -c access.log.*.gz >> ~/visitors.txt

visitors = open('visitors.txt', 'r')
c = 1

for line in visitors:
    fields = line.strip().split()

    status_code = fields[8]
    requested = fields[6]

    if status_code == "200":
        if not ".svg" or ".img" or ".png" or ".css" in requested:
	    if requested != "*":
		c+=1
		#print requested

print c
