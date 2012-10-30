def oweAmount(b0, r, m):
	return (b0-(b0*m))*(1+(r/12))

total = 0

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(12):
	print("Month: " + str(month+1))
	z = oweAmount(balance, annualInterestRate, monthlyPaymentRate)
	print("Minimum monthly payment: " + str(round(balance*monthlyPaymentRate,2)))
	print("Remaining balance: " + str(round(z,2)))
	total += balance*monthlyPaymentRate
	balance = z

print("Total paid: " + str(round(total,2)))
print("Remaining balance: " + str(round(balance,2)))

