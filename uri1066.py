fnum = []
fnum.append(int(input()))
fnum.append(int(input()))
fnum.append(int(input()))
fnum.append(int(input()))
fnum.append(int(input()))



def evn():
    y = 0
    for x in fnum:
        if x%2 == 0:
            y += 1
    print("%d valor(es) par(es)" %y)

def odd():
    y = 0
    for x in fnum:
        if x%2 != 0:
            y += 1
    print("%d valor(es) impar(es)" %y)

def pos():
    y = 0
    for x in fnum:
        if x> 0:
            y += 1
    print("%d valor(es) positivo(s)" %y)

def neg():
    y = 0
    for x in fnum:
        if x<0:
            y += 1
    print("%d valor(es) negativo(s)" %y)

evn()
odd()
pos()
neg()