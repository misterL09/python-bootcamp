import datetime
import time


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.task = []
        self.timein = datetime.time
        self.timeout = datetime.time
        self.remark = f"new create employee: {name} {id}"
        print(self.remark)
    def time_in(self,time):
        self.timein = time
        print(f"time in: {self.name} {self.id} ", time)
    def time_out(self, time):
        self.timeout = time
        print(f"time out: {self.name} {self.id} ", time)

class Recruiter(Employee):
    def recruit(self):
        self.remark =  f"new create recruiter: {self.name} {self.id}"
        print("doing recruit")

class Developer(Employee):
    def manage(self):
        self.remark =  f"new create developer: {self.name} {self.id}"
        print("doing developer")

employee = Employee("nathan","001")
employee.time_in(datetime.time())
employee.time_out(datetime.time())
recruiter = Recruiter("ken","002")
recruiter.recruit()
recruiter.time_in(datetime.time())
recruiter.time_out(datetime.time())

