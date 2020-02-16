A,B,C =input().split()
A = float(A)
B = float(B)
C = float(C)

D = A*A
E = B*B
F = C*C

if A >= B + C:
	print("NAO FORMA TRIANGULO")
if D==E+F:
	print("TRIANGULO RETANGULO")
if D>E+F:
	print("TRIANGULO OBTUSANGULO")
if D<E+F:
	print("TRIANGULO ACUTANGULO")
if A==B and B==C and A==C:
	print("TRIANGULO EQUILATERO")
if A==B or B==C or A==C:
	print("TRIANGULO ISOSCELES")