
def arrNum(x):
    x = float(x)
    i = 0
    print("N[%d] = %.4f"%(i,x))
    for i in range(99):
        i += 1
        y = x/2
        y = float(y)
        print("N[%d] = %.4f"%(i,y))
        x = y

    return i,y,x

k = float(input())
arrNum(k)
        