def ft_abs():
	expression = input("Insert an expression: ")

	try:
		result = eval(expression)
		
		if result < 0:
			result = -result

		print("The result is:", result)
	except Exception:
		print("Error! Usage: insert a valid expression.")

if __name__ == "__main__":
	ft_abs()
