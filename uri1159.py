n = 1
while n>0:
    v = 0
    x = int(input())
    j = x
    m = 1
    u = 5
    while m<=u:
        if j%2 == 0:
            v += j
            j += 1
            m += 1
    
    
        elif j%2 != 0:
            j += 1
        
    if x==0:
        n = 0
        break
    n += 1
    print(v)
    
            
            
        

    