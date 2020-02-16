m = [1,2,3]
n = [2,3,4]
o = [3,4,5]

i = 0
j = 0
k = 0

a = m[i]
b = n[j]
c = o[k]

while i<3:
    while j<3:
        while k<3:
            print('%d %d %d'%(a,b,c))
            i += 1
            j += 1
            k += 1