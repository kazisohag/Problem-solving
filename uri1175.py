l = []
for i in range(20):
    x = int(input())
    l.append(x)

V = reversed(l)
i = 0
for x in V:
    print("N[%d] = %d" %(i,x))
    i += 1
    