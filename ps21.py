def oweAmount(b0, r, m):
	return (b0-m)*(1+(r/12))

def calculateMinimum(x):
	coiso = balance
	for month in range(12):
		z = oweAmount(coiso, annualInterestRate, x)
		coiso = z
	if coiso > 0:
		return calculateMinimum(x+10)
	else:
		return x

print("Lowest Payment: " + str(calculateMinimum(10)))