import pickle

def dump_word_dict():
	try:
		with open("words.txt", "r") as file:
			words = [line.strip() for line in file]
	except:
		print("Error! The specified file does not exist!")
		return
	
	word_dict = {}
	for word in words:
		length = len(word)
		if length in word_dict:
			word_dict[length] += 1
		else:
			word_dict[length] = 1

	with open('word_count.pickle', 'wb') as handle:
		pickle.dump(word_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
	dump_word_dict()
