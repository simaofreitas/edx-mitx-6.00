x = int(raw_input("Enter a number: "))
if x%2 == 0:
	if x%3 == 0:
		print(" ")
		print("DIvisivel por 2 e 3")
	else:
		print(" ")
		print("DIvisivel por 2 mas nao 3")
elif x%3 == 0:
	print(" ")
	print("Divisivel por 3 mas nao 2")
else:
	print("Nao divisivel por 2 ou 3")