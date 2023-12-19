import sys

def trim(l):
	del l[0]
	del l[len(l) - 1]

def ft_trim():
	if len(sys.argv) < 3:
		print("Error! You must insert at least 2 values")
		return
	l = [x for x in sys.argv[1:]]
	trim(l)
	print("The new list is:", l)

if __name__ == '__main__':
	ft_trim()
