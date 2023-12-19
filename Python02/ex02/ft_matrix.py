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

def ft_matrix():
	if len(sys.argv) < 3 or len(sys.argv) > 3:
		print("Error! Usage: python3 ft_matrix.py <n> <m>")
		return

	try:
		n = int(sys.argv[1])
		m = int(sys.argv[2])
	except ValueError:
		print("Error! Usage: python3 ft_matrix.py <n> <m>")
		return

	matrix = [[0] * m for _ in range(n)]

	for i in range(n):
		for j in range(m):
			matrix[i][j] = float(input("Insert the element in position (" + ft_itoa(i) + ", " + ft_itoa(j) + "): "))

	print("The inserted matrix is:")
	for row in matrix:
		print(row)

	row_sums = []
	for row in matrix:
		row_sum = 0
		for num in row:
			row_sum += num
		row_sums = row_sums + [row_sum]
	print("The sum over rows is:")
	print(row_sums)

	col_sums = []
	for j in range(m):
		col_sum = 0
		for i in range(n):
			col_sum += matrix[i][j]
		col_sums = col_sums + [col_sum]
	print("The sum over columns is:")
	print(col_sums)


if __name__ == '__main__':
	ft_matrix()
