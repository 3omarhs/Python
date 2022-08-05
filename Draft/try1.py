import datetime
x = datetime.datetime.now()
class Person:
    def __init__(self,name,birth_year):
        self.name=name
        self.birth_year=birth_year
    def print_info(self):
        age=x.year-self.birth_year
        print(f"This is {self.name} and his/her age is {age}")
p1=Person("ahmad",2003)
p1.print_info()