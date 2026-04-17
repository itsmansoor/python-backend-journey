#Basic Function
def Greet():
    print("Hello")
    print("Good Morning")

Greet()

#function with parameter
def greet(name):
    print("Hello", name)

greet("Mansoor")

#function with parameters
def Add(a,b):
    c = a + b
    print(c)

Add(2,3)

#function with Return 
def add(a, b):
    return a + b

result = add(2, 3)
print(result)

#Default Parameters
def greet(name="Guest"):
    print("Hello", name)

greet()          # Guest
greet("Ali")     # Ali

#Keyword Arguments
def student(name, age):
    print(name, age)

student(age=22, name="Mansoor")


def login(username, password):
    if username == "admin" and password == "123":
        return "Login Successful"
    else:
        return "Login Failed"

print(login("admin", "123"))


#scope 
a = 20

def something():
   # a = 6 local
    global a
    a = 23
    print('func ' ,a)

something(a)
print('outside',a)