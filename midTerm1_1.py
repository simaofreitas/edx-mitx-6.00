def myLog(x, b):
  '''
  x: a positive integer
  b: a positive integer; b >= 2

  returns: log_b(x), or, the logarithm of x relative to a base b.
  '''
  exp = 0
  while b**exp <= x:
      exp += 1
  return exp-1

# print myLog(16,2) #4
# print myLog(15,3) #2
# print myLog(20,2) #4
# print myLog(33,2) #5


def laceStrings(s1, s2):
  """
  s1 and s2 are strings.

  Returns a new str with elements of s1 and s2 interlaced,
  beginning with s1. If strings are not of same length,
  then the extra elements should appear at the end.
  """
  i = 0
  final = ""
  while i < len(s1) and i < len(s2):
    final += s1[i]
    final += s2[i]
    i += 1
  if i < len(s1):
    final += s1[i:]
  elif i < len(s2):
    final += s2[i:]
  return final

# print laceStrings("aaa", "bbb") #ababab
# print laceStrings("abc", "defgh") #adbecfgh
# print laceStrings("a", "bbb") #abbb
# print laceStrings("aaa", "b") #abaa
# print laceStrings("", "bbb") #bbb

def laceStringsRecur(s1, s2):
  """
  s1 and s2 are strings.

  Returns a new str with elements of s1 and s2 interlaced,
  beginning with s1. If strings are not of same length,
  then the extra elements should appear at the end.
  """
  def helpLaceStrings(s1, s2, out):
    if s1 == '':
        return s2
    if s2 == '':
        return s1
    else:
        return s1[0] + s2[0] + helpLaceStrings(s1[1:], s2[1:], '')
  return helpLaceStrings(s1, s2, '')

# print laceStringsRecur("LOL","") #LOL
# print laceStringsRecur("L", "OL") #LOL
# print laceStringsRecur("aaa", "bbb") #ababab
# print laceStringsRecur("abc", "defgh") #adbecfgh
# print laceStringsRecur("a", "bbb") #abbb
# print laceStringsRecur("aaa", "b") #abaa
# print laceStringsRecur("", "bbb") #bbb

def McNuggets(n):
  """
  n is an int

  Returns True if some integer combination of 6, 9 and 20 equals n
  Otherwise returns False.
  """
  a = 0
  b = 0
  c = 0
  if n <= 0:
    return False
  if n%6 == 0 or n%9 == 0 or n%20 == 0:
    return True
  while a*6+b*9+c*20 < n:
    for i in range(n%20):
      for j in range(n/9 - n/20):
        for k in range(n/6 - n/9 - n/20):
          if 6*a+9*b+20*c == n:
            return True
          a += 1
        b += 1
      c += 1
  return False

# print McNuggets(6)
# print McNuggets(27)
# print McNuggets(20)
# print McNuggets(1704)
# print McNuggets(1716)
# print McNuggets(2715)
# print McNuggets(0)
# print McNuggets(4)
# print McNuggets(7)

