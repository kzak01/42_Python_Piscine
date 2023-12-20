class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return "({}, {})".format(self.x, self.y)

class Circle:
	def __init__(self, center=Point(), radius=0):
		self.center = center
		self.radius = radius

	def __str__(self):
		return "Circle of center {} and radius {}".format(self.center, self.radius)

def circle():
	circle = Circle(Point(150, 100), 75)
	print(circle)

if __name__ == '__main__':
	circle()
