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

def ft_char_count():
	if len(sys.argv) != 2:
		print("Error! No string given")
		return

	char_dict = dict()
	string = sys.argv[1]

	for char in string:
		if char not in char_dict:
			char_dict[char] = 0

	for char in string:
		char_dict[char] += 1

	print("Char count:")
	for char in " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~":
		if char in char_dict:
			print(char + " = " + ft_itoa(char_dict[char]))

if __name__ == "__main__":
	ft_char_count()
