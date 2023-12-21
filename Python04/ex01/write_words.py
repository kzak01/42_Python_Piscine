def ft_atoi(s):
	ascii_map = {'0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57}
	result = 0
	negative = False

	if s[0] == '-':
		negative = True
		s = s[1:]

	for digit in s:
		if '0' <= digit <= '9':
			result = result * 10 + (ascii_map[digit] - 48)
		else:
			return None

	if negative:
		result = -result

	return result

def print_words():
	try:
		with open('words.txt', 'r') as file:
			words = [line.strip() for line in file]
	except:
		print("Error: file not found")
		return

	n = ft_atoi(input("Insert an integer: "))
	if n is None:
		print("Error: invalid input")
		return

	long_words = [word for word in words if len(word) > n]
	long_words.sort()

	print("The words longer than {} have been written on \"long_words.txt\"".format(n))
	for word in long_words:
		with open('long_words.txt', 'a') as file:
			file.write(word + "\n")

if __name__ == '__main__':
	print_words()
