def ft_space_print():
	s = input("Insert a string: ")
	column = 20

	if len(s) > column:
		s = s[-column:]
	else:
		s = ' ' * (column - len(s)) + s

	print(s)

if __name__ == '__main__':
	ft_space_print()
