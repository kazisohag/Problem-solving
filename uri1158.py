N = int(input())
v = 0
for i in range(N+1):
    linha1 = input().split(" ")
    x,y = linha1
    x = int(x)
    y = int(y)
    
    j = x
    m = 1
    while m<=y:
        if j%2 != 0:
            v += j
            j += 1
            m += 1
        else:
            j += 1
    print(v)

    