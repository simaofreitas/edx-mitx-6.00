def oweAmount(b0, r, m):
	return (b0-m)*(1+(r/12))

def lowestBound(x):
	return x/12

def highBound(x,r):
	return (x*(1+r/12)**12)/12

def calculateMinimum(low,high):
	coiso = balance
	ans = (high+low)/2
	for month in range(12):
		z = oweAmount(coiso, annualInterestRate, ans)
		coiso = z
	if abs(0-coiso) > 0.01:
		if coiso < 0:
			high = ans
			return calculateMinimum(low,high)
		else:
			low = ans
			return calculateMinimum(low,high)
	else:
		return ans

low1 = lowestBound(balance)
high1 = highBound(balance, annualInterestRate)

print("Lowest Payment: " + str(round(calculateMinimum(low1, high1),2)))