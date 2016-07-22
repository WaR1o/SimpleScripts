class Cylinder(object):
	
	

	def __init__(self,height=1,radius=1):
		self.height = height
		self.radius = radius

	def volume(self):
		pi = 3.141592
		vol = pi*(self.radius**2)*self.height
		print(vol)

	def surface_area(self):
		pi = 3.141592
		sur_a = 2*pi*self.radius**2 + 2*pi*self.radius*self.height
		print(sur_a)


c = Cylinder(2,3)
c.volume()
c.surface_area()


