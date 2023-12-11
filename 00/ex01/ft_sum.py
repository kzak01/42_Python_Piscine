def ft_strlen(s):
	length = 0
	while s[length:]:
		length += 1
	return length

def ft_abs(n):
	if n < 0:
		return -n
	return n

def atoi(s):
	result = 0
	sign = 1
	i = 0

	if s[0] == '-':
		sign = -1
		i = 1
	elif s[0] == '+':
		i = 1

	while i < ft_strlen(s) and s[i].isdigit():
		result = result * 10 + int(s[i])
		i += 1

	return sign * result

def itoa(n):
	result = ""
	sign = 1

	if n < 0:
		sign = -1
		n = ft_abs(n)

	while n > 0:
		digit = n % 10
		result = str(digit) + result
		n //= 10

	if sign == -1:
		result = '-' + result

	return result

def main():
	print("Insert your first number: ")
	first = input()
	print("Insert your second number: ")
	second = input()
	print("Result: " + itoa(atoi(first) + atoi(second)))

if __name__ == '__main__':
	main()
