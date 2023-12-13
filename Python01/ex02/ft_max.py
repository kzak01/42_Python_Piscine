import sys

def ft_max():
	if len(sys.argv) != 4:
		print("Error! Usage: python3 ft_max.py <x> <y> <z>")
		return

	try:
		x = float(sys.argv[1])
		y = float(sys.argv[2])
		z = float(sys.argv[3])
	except ValueError:
		print("Error! Usage: python3 ft_max.py <x> <y> <z>")
		return

	max = x
	if max < y:
		max = y
	if max < z:
		max = z

	print("The maximum number is:", max)

if __name__ == "__main__":
	ft_max()
