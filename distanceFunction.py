import math
x1 = float(input("Please Enter x for 1st : "))
y1 = float(input("Please Enter y for 1st : "))

x2 = float(input("Please Enter x for 2nd : "))
y2 = float(input("Please Enter y for 2nd : "))


def distance_dots(x1,y1,x2,y2):
    dis = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    print("distance is ",dis)
    return dis

distance_dots(x1,y1,x2,y2)