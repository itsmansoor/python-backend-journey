# error handling or protect the app from crashing 

try:
    a = 10
    b = 0
    print(a / b)
except:
    print('error occured')


#2. Specific Exception

try:
    num = int('abc')
except ValueError:
    print('invalid Input')

#3. Multiple Exceptions 
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print('can not divide by zere')
except ValueError:
    print('value error')


#4 else 
try:
    a = 10
    b = 2
    print(a / b)
except:
    print("Error")
else:
    print("No error")

#5. finally

try:
    print("Hello")
except:
    print("Error")
finally:
    print("Done")


#6. Custom Exception
age = -1

if age < 0:
    raise Exception("Age cannot be negative")
