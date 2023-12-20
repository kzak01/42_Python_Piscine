class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

def point():
	try:
		x1, y1 = eval(input("Insert the coordinates of the first point: "))
		x2, y2 = eval(input("Insert the coordinates of the second point: "))
		p1 = Point(x1, y1)
		p2 = Point(x2, y2)
		distance = ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
		print("Their distance is: {}".format(distance))
	except ValueError:
		print("Error: Invalid input")

if __name__ == '__main__':
	point()
