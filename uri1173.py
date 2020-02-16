v = int(input())
x = v
if v < 50:
    print("N[%d] = %d" %(0,x))
    for i in range(1,10):
        y = x*2
        print("N[%d] = %d" %(i,y))
        x = y