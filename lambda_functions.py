__author__ = 'Ahadu Tsegaye Abebe - 09/07/17'
#lambda arguments: expression

#lambda with name binding
sum = lambda x, y: x+y
print (sum(3,5))


#without name binding: MAP
print(map(lambda x:x**2+3, range(10)))

#FILTER
y = map(lambda x:x**2+3, range(10))
print(filter(lambda x: x%2==0, y))


#REDUCE


