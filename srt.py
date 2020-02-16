v = [8,4,3,6,9]
l = []
i = 0
j = 1

while i < len(v):
    if v[i] > v[j]:
        v[i] = v[j]
        n = v[i]
        l.append(n)
    
    i += 1
    j += 1
    
print(l)
