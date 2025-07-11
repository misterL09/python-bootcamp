class Student:
	def __init__(self, name, level):
		self.name = name
		self.level = level

	def introduce(self):
		return f"I'm {self.name}! I'm a {self.level} student."

student1 = Student("Juan", '3rd Year College')
print(student1.introduce())

student2 = Student("Maria", 'Grade Three')
print(student2.introduce())

