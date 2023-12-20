import sys

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

	def contains(self, point=Point(0, 0)):
		if ((point.x - self.center.x)**2 + (point.y - self.center.y)**2) <= self.radius**2:
			return True
		else:
			return False

def circle():
	if len(sys.argv) != 3:
		print("Error: Invalid number of arguments")
		return

	try:
		point = Point(float(sys.argv[1]), float(sys.argv[2]))
		circle = Circle(Point(0, 0), 1)

		if circle.contains(point):
			print("The point {} lies in the {}".format(point, circle))
		else:
			print("The point {} lies out of the {}".format(point, circle))
	except ValueError:
		print("Error: Invalid input")

if __name__ == '__main__':
	circle()
