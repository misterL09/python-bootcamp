from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    age: int


x = Employee("nathan",25)
print(x.name)