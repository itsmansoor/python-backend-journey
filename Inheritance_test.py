class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def Bark(self):
        print('dog barks')

d = Dog()
d.sound
d.Bark

# Multilevel Inheritance
class A:
     def feature1(self):
        print("feaature 1 is working")
     def feature2(self):
            print("feature 2 is working")

class B(A):
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")


class C(B):
     def feature5(self):
          print('feature 5 is working')


a1 = A()
a1.feature1
a1.feature1

b1= B()
b1.feature1
b1.feature2
b1.feature3
b1.feature4

c1 = C()
c1.feature1
c1.feature2
c1.feature3
c1.feature4
c1.feature5

#Multiple Inheritance
class Father:
    def skills(self):
        print("Coding")

class Mother:
    def skills2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()
c.skills2()

#constructor in inheeritance
class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        print("Child Constructor")

c = Child()   #Child Constructor

 #Using super()
class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

c = Child() #parent constructor
            #child constructor