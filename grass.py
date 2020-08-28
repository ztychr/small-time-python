while True:
        
    import math

    n = raw_input().split()

    sets = []
    intervalstmp = []

    sprinks = int(n[0])
    target  = [0, int(n[1])]
    width  = int(n[2])

    def getB(a, c):
        b = math.sqrt(c*c-a*a)
        return b

    for i in range(0, int(sprinks)):
        num = raw_input().split()
        n1 = int(num[0])
        n2 = int(num[1])

        sets.append([n1, n2])

    for i in range(0, len(sets)):

        acc = 0
        sideC = sets[i][1]
        b = getB(float(width)/float(2), float(sideC))
        pos = float(sets[i][0])
        tmplist = [pos-b, pos+b]
        intervalstmp.append(tmplist)
        acc+=1

    #print intervalstmp

    def getmax(liste, t):
        big = -1
        for n in liste:
            index = liste.index(n)
            if n[0] <= t:
                if n[1] >= big:
                    big = n[1]
                    start = n[0]

        res = (start,big)
    # list.index([start,big])
        return big, res

    intervalstmp.sort(key= lambda x : x[1])
    S = []
    t = target[0]
    while t < target[1]:

        try:
            get, i  = getmax(intervalstmp, t)
            S.append(i)
            t = get
            
        except StandardError as e:
            break

    if len(S) == 0:
        print "-1"
    else: 
        print len(S)
