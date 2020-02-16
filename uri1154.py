i = 1
s = 0
n = 0
while i>0:
	x = int(input())
	
	if x>=0:
		s += x
		n += 1
			 
	elif x<0:
		i = x-5
	i += 1
	
t = s/n	
print("%.2f" %t)
