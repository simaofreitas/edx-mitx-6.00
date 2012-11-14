def isPrime(n)
  if not isinstance(n,int):
      raise TypeError()
  elif n <= 0:
      raise ValueError()
  for i in range(2,n-1):
    if n%i==0:
      return False
  return True
