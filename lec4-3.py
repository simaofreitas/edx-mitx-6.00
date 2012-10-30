x = 25

epsilon = 0.01

step = epsilon**2

numGuesses = 0
ans = 0.0

while(abs(ans**2 - x)) >= epsilon and ans <= x:
	ans += step
	numGuesses += 1

print("Guesses: " + str(numGuesses))
if abs(ans**2 - x) >= epsilon:
	print("Failed on square root of " + str(x))
else:
	print(str(ans) + " is close to the square root of " + str(x))