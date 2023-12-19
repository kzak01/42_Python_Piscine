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

def ft_sum():
	first_int = ft_atoi(input("Insert your first integer: "))
	second_int = ft_atoi(input("Insert your second integer: "))

	if first_int is None or second_int is None:
		print("Error: Both inputs must be valid integers")
	else:
		result = first_int + second_int
		print("Result:", ft_itoa(result))

if __name__ == '__main__':
	ft_sum()
