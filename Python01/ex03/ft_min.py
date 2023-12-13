import sys

def my_min(x=0, y=0, z=0):
	min = x
	if y < min:
		min = y
	if z < min:
		min = z

	return min

def ft_min():
	if len(sys.argv) != 4:
		print("Error! Usage: python3 ft_min.py <x> <y> <z>")
		return
	try:
		x = float(sys.argv[1])
		y = float(sys.argv[2])
		z = float(sys.argv[3])
	except ValueError:
		print("Error! Usage: python3 ft_min.py <x> <y> <z>")
		return

	min = my_min(x, y, z)

	print("The min is:", min)

if __name__ == "__main__":
	ft_min()
