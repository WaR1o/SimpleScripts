from math import sqrt


class Line(object):
	
	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		a = self.coor2[0]-self.coor1[0]
		b = self.coor2[1]-self.coor1[1]		
		c = sqrt(a**2 + b**2)
		return c

	def slope(self):
		a = self.coor2[0]-self.coor1[0]
		b = self.coor2[1]-self.coor1[1]		
		c = b/a
		return c

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())
