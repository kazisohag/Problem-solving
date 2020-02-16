i = 0
l = []
even = []
odd = []
while i<15:

    x = int(input())
    l.append(x)
    i += 1

for y in l:

    
    if y%2 == 0:
        even.append(y)
    
    else:
        odd.append(y)


v = 0
while v<5:
    evenL = even[v]
    print("par[%d] = %d"%(v,evenL))

    v += 1

t = 0
while t<5:
    oddL = odd[t]
    print("impar[%d] = %d"%(t,oddL))

    t += 1


if len(odd)>5:
    a = 0
    for u in range(5,len(odd)):
        oddu = odd[u]
        print("impar[%d] = %d"%(a,oddu))
        a += 1


if len(even)>5:
    c = 0
    for b in range(5,len(even)):
        evenU = even[b]
        print("par[%d] = %d"%(c,evenU))
        c += 1



