import sys

def is_palindrome(msg=None):
	i = 0
	j = len(msg) - 1
	while i < j:
		if (msg[i] == ' '):
			i += 1
			continue
		if (msg[j] == ' '):
			j -= 1
			continue
		if msg[i] != msg[j]:
			return False
		i += 1
		j -= 1
	return True

def ft_palindrome():
	if len(sys.argv) < 2 or len(sys.argv) > 2:
		print("Error! Insert just 1 string!")
		exit()
	if is_palindrome(sys.argv[1]) == True:
		print("The string " + sys.argv[1] + " is palindrome")
	else:
		print("The string " + sys.argv[1] + " is not palindrome")

if __name__ == '__main__':
	ft_palindrome()
