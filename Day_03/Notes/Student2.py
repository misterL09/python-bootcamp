class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def sleep(self):
        print("I will sleep for eight hours")
    def silent_sleep(self):
        print("I will sleep for eight hours")
    def introduce(self):
        return f"I'm {self.first_name} {self.last_name}!"

class Student(Person):
    def __init__(self, first_name, last_name, level):
        super().__init__(first_name, last_name)
        self.level = level
    def introduce(self):
        return super().introduce() + f" I'm a {self.level} student."
    def silent_sleep(self):
        print("I will sleep for six hours")

person = Person("nathan","medalla")
student = Student(person.first_name,person.last_name,4)

print(student.sleep())
print(student.silent_sleep())
