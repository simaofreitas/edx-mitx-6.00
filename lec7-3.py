def printMove(fr, to):
	print("move from " + str(fr) + " to " + str(to))

def towersn(n, fr, to, spare):
	if n == 1:
		return printMove(fr, to)
	else:
		towersn(n-1, fr, spare, to)
		towersn(1, fr, to, spare)
		towersn(n-1, spare, to, fr)

print(str(towersn(3, 2, 1, 3)))