class Coordinate(object):
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def __str__(self):
    return "<" + self.x + ", " + self.y + ">"
