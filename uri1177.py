def vector(a):
    if a>=2 or a<=50:
        i = 0
        j = 0
        while i<1000:
            while j<a:

                print('N[%d] = %d' %(i,j))

                i += 1
                j += 1
            
                if i > 999:
                  break
            j = 0
        
        
    return i,j,a

x = int(input())

v = vector(x)