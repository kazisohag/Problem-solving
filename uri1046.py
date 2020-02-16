A,B =input().split()
A = int(A)
B = int(B)

if A>12:
	x = (24-A)+B
	print("O JOGO DUROU",x,"HORA(S)")
elif A<=12  and A!=B:
  x = (B-A)
  print("O JOGO DUROU",x,"HORA(S)")
elif A==B:
  x = (B-A)+24
  print("O JOGO DUROU",x,"HORA(S)")