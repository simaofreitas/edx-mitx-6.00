x = float(raw_input("Enter a number: "))
p = int(raw_input("Enter the power: "))

result = 1

def iterativePower(x,p):
	'''
	computes the power p of number x
	'''
	result = 1

	for turn in range(p+1):
		print("Iteration: " + str(turn) + \
			"current result: " + str(result))
		result = result * x
	return result

#call function (output comes from function)
iterativePower(x,p)