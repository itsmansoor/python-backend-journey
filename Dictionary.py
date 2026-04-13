data = {1:'Rasool',
        2:'yasir',
        3:'Mutahar Hussain',
        4:'Mansoor'
        }
print(data)


print(data[3])  #Mutahar Hussain

student = {
    "name": "Mansoor",
    "age": 22,
    "course": "IT"
}

print(student["name"])   # Mansoor

print(student.get("age"))   # 22

student["city"] = "Lahore"   # add
student["age"] = 23          # update

student.pop("age")

del student["course"]

print(student.keys())
print(student.values())

users = {
    "user1": {"name": "Ali", "age": 20},
    "user2": {"name": "Ahmed", "age": 25}
}

print(users["user1"]["name"]) 