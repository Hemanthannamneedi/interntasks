# Coding Task:
class Student:
    def __init__(self,stud_id, name, marks):
        self.stud_id = stud_id
        self.name = name
        self.marks = marks
    def display_details(self):
        print("Student ID: ",self.stud_id)
        print("Stud_Name: ",self.name)
        print("Marks: ",self.marks)
std1 = Student(503,"Priyanka",76)
std1.display_details()

# Assignment:
class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    def display_profile(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("City: ",self.city)
p1 = Person("Hemanth",21,"Bapatla")
p1.display_profile()
