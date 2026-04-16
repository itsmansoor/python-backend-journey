import array

arr1 = array.array('i',[1,23,4,5,6,7,8])
print(arr1)
 

n = int(input("Enter size: "))
arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)


search  = int(input("Enter number to search: "))

if search in arr:
    print("Element found at index:", arr.index(search))
else:
    print("Element not found")
print(arr)