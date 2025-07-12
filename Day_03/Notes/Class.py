class Employee:
    """class representation for employee data"""
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print("Employee Created")
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        return self.tasks.append(task)

employee1 = Employee("Ken",123)
employee2 = Employee("Nathan","124")
employee1.add_work("coffee break")


print("Employee 1 Name:", employee1.name)
print("Employee 2 Name:", employee2.name)
print("Employee 1 Name:", *employee1.tasks)

