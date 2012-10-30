x = int(raw_input('Enter an integer: '))
ans = 0

while(ans**3 < abs(x)):
	ans = ans + 1

if ans**3 != abs(x):
	print(str(x) + " is not a perfect cube. The best value is " + str(ans))
else:
	if x < 0:
		ans = -ans
	print("The cube root of " + str(x) + " is " + str(ans))