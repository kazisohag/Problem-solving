class number:
    a = 100
    b = 200

class add(number):
    n = number()
    c = n.a + n.b

p = add()
print(' c = ',p.c)
