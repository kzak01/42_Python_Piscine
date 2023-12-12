def ft_print():
	string = input("Insert a string: ")
	columns = 20
	
	if len(string) > columns:
		string = string[-columns:]
	else:
		string = ' ' * (columns - len(string)) + string

	print(string)

if __name__ == '__main__':
	ft_print()
