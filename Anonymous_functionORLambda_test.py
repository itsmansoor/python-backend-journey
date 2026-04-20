from functools import reduce
add = lambda a,b: a + b;
print(add(3,4))

square = lambda x: x * x
print(square(5)) 


# filter method
nums = [1,2,3,4,5,6,7,8,9,10]

# even = list(filter(lambda n: n%==0,nums))
even = list(filter(lambda n: n%2==0,nums))
print(even)

#map method 
double = list(map(lambda n: n*2,even))
print(double)

#reduce method 
sum = reduce(lambda a,b,:a+b,double)
print(sum)