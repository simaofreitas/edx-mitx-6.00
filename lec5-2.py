epislon = 0.01
y = 25.0
guess = y/2.0

while abs(guess*guess - y) >= epislon:
	guess = guess - (((guess**2) - y)/(2*guess))

print("Square root of " + str(y) + " is about " + str(guess))