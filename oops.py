class Student:

    def __init__(self,name):
        self.name = name


std1 = Student("Mansoor")
print(std1.name)


class car:

    def __init__(self,brand):
        self.Brand = brand

car1 = car("Toyota")
print(car1.Brand)

#Instance vs Class Variable

class student:
    
    University = 'The Agriculture University OF Peshawar' #class veriable

    def __init__(self,name):
        self.name = name  #instance veriable

Std1 = student("Khaksar")
print(std1.name)
print(student.University)


#instance method 
class Demo:
    def show(self):
     print("instance method")

d = Demo()
d.show()

#class method 

class Demo:
    @classmethod
    def show(cls):
        print("class method")

Demo.show()

#static method 
class Demo:
    @staticmethod
    def show():
        print("Static method")

#Demo.show()
d = Demo()
d.show()