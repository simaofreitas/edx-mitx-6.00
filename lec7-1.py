def factR(x):
	"""
	Assumes n is int and n >= 1
	"""
	if x == 1:
		return x
	else:
		return x*factR(x-1)

print("Factorial of 4: " + str(factR(4)))