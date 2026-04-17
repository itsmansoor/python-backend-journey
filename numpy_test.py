import numpy as np

arr = np.array([1, 2, 3])
print(arr)


print(arr + 2)
print(arr * 2)

print(arr[1])


arr2 = np.array([[1, 2,3], [4, 5,6]])
print(arr2)

arr3 = arr2.flatten()
print(arr3)

print(arr2.shape)  
print(arr2.size)   
print(arr2.ndim)    


print(np.zeros(3)) 
print(np.ones(3))    
print(np.arange(1, 5))



arr4 = np.array([10, 20, 30])

print("Sum:", arr4.sum())
print("Mean:", arr4.mean())