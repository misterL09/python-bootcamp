class Employee:
    """Class representation for employee data"""
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print(f"Employee {self.name} created with ID {self.id}")

employee1 = Employee("Richard", "1234")
employee2 = Employee("Jelly", "9876")

print("Employee 1 Name:", employee1.name)
print("Employee 2 Name:", employee2.name)




