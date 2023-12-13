import sys

def ft_compare():
	if len(sys.argv) != 3:
		print("Error! Usage: python3 ft_compare.py <x> <y>")
		return

	try:
		num1 = float(sys.argv[1])
		num2 = float(sys.argv[2])
	except ValueError:
		print("Error! Usage: python3 ft_compare.py <x> <y>")
		return

	if num1 > num2:
		print(num1, "is greater than", num2)
	elif num1 < num2:
		print(num1, "is less than", num2)
	else:
		print(num1, "is equal to", num2)

if __name__ == "__main__":
	ft_compare()
