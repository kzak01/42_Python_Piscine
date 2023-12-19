import sys

def ft_sorted():
	if (len(sys.argv) < 3):
		print("Error! You must insert at least 2 numbers")
		return
	
	try:
		numbers = [int(x) for x in sys.argv[1:]]
		sort_num = [int(x) for x in sys.argv[1:]]
	except ValueError:
		print("Error! You must insert only numbers")
		return
	sort_num = sorted(sort_num, reverse = True)

	i = 0
	while i < len(numbers):
		if (numbers[i] != sort_num[i]):
			print("The inserted sequence is not sorted!")
			print("The correct order is", sort_num)
			return
		i += 1

	print("The inserted sequence is sorted!")

if __name__ == '__main__':
	ft_sorted()
