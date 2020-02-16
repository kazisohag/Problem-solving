a = float(input())
if a >= 0 and a <= 400.00:
	b = a*0.15
	x = b+a
	print("Novo salario: %.2f" %x)
	print("Reajuste ganho: %.2f" %b)
	print("Em percentual: 15 %")
elif a >= 400.01 and a <= 800.00:
	b = a*0.12
	x = b+a
	print("Novo salario: %.2f" %x)
	print("Reajuste ganho: %.2f" %b)
	print("Em percentual: 12 %")
elif a >= 800.01 and a <= 1200.00:
	b = a*0.10
	x = b+a
	print("Novo salario: %.2f" %x)
	print("Reajuste ganho: %.2f" %b)
	print("Em percentual: 10 %")
elif a >= 1200.01 and a <= 2000.00:
	b = a*0.07
	x = b+a
	print("Novo salario: %.2f" %x)
	print("Reajuste ganho: %.2f" %b)
	print("Em percentual: 7 %")
elif a > 2000.00:
	b = a*0.04
	x = b+a
	print("Novo salario: %.2f" %x)
	print("Reajuste ganho: %.2f" %b)
	print("Em percentual: 4 %")
	