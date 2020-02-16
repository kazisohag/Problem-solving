while True:
    try:
        m,n = list(map(int,input().split()))
        if(m < 1 or n < 1 ):
            break
        i = 0

        if(m > n):
            i = m
            m = n
            n = i
        t = 0
        x = ''
        while(m <= n):
            x += str(m) + ' '
            t += m
            m += 1
        x += 'Sum=%d'
        print(x %t)
    except:
        break