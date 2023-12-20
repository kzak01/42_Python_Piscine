class Person:
	def __init__(self, name, last_name):
		self.name = name
		self.last_name = last_name

	def __str__(self):
		return "{} {}".format(self.name, self.last_name)
	
class Student(Person):
	def __init__(self, name, last_name, course=None):
		Person.__init__(self, name, last_name)
		self.course = course

	def __str__(self):
		if self.course == "":
			return "{} {} is not registered to any course".format(self.name, self.last_name)
		return "{} {} is registered to {}".format(self.name, self.last_name, self.course)

def student():
	name = input("Insert first name: ")
	last_name = input("Insert last name: ")
	question = input("Are you a student? (y/n)")

	flag = False
	while flag != True:
		if question == "y" or question == "n":
			flag = True
		else:
			question = input("Please type \"y\" or \"n\": ")

	if question == "y":
		course = input("Please insert your degree course: ")
		student = Student(name, last_name, course)
		print(student)
	else:
		person = Person(name, last_name)
		print(person)

if __name__ == '__main__':
	student()
