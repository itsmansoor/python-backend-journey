fruits = ['Orange','Banana','Apple','Mongo']
print(fruits)

print(fruits[0])

fruits.append("chery") #adding item or elements at the end
print(fruits)

fruits.remove("Apple")  #removing item or elements 
print(fruits)

fruits[0]= "grapes" #changing item or elements 
print(fruits)

fruits.extend(["abc","xyz"])
print(fruits)

list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1)

nums = [8,7,6,4,2,1]
nums.sort()   #sorting items or elments 
print(nums)