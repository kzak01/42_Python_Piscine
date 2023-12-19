import sys

def ft_itoa(n):
	if n == 0:
		return '0'
	ascii_map = {48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9'}
	result = ''
	negative = False

	if n < 0:
		negative = True
		n = -n

	while n > 0:
		result = ascii_map[(n % 10) + 48] + result
		n = n // 10

	if negative:
		result = '-' + result

	return result

# def ft_duplicates(numList):
# 	i = 0
# 	while i < len(numList):
# 		j = i + 1
# 		while j < len(numList):
# 			if numList[i] == numList[j]:
# 				return True
# 			j += 1
# 		i += 1
# 	return False

def ft_max_pos(numList):
	maxPos = 0
	i = 1
	while i < len(numList):
		if numList[i] > numList[maxPos]:
			maxPos = i
		i += 1
	return maxPos

def ft_min_pos(numList):
	minPos = 0
	i = 1
	while i < len(numList):
		if numList[i] < numList[minPos]:
			minPos = i
		i += 1
	return minPos

def ft_ext_pos():
	if len(sys.argv) < 2:
		print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
		return

	try:
		numList = [int(num) for num in sys.argv[1:]]
	except ValueError:
		print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
		return

	# if ft_duplicates(numList):
	# 	print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
	# 	return

	numMaxPos = ft_max_pos(numList)
	numMinPos = ft_min_pos(numList)

	print("The min is " + ft_itoa(numList[numMinPos]) + " and its position is " + ft_itoa(numMinPos))
	print("The max is " + ft_itoa(numList[numMaxPos]) + " and its position is " + ft_itoa(numMaxPos))

if __name__ == '__main__':
	ft_ext_pos()
