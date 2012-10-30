def gcdIter(x,y):
	z = min(x,y)
	while (x%z!=0 or y%z!=0):
		z -= 1
	return z

print(str(gcdIter(30,4)))