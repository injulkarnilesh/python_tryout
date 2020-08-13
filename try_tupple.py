
#tuples are immutable iterable data types
tuple_one = 1,2,"who",56,"me"
print(tuple_one) #(1, 2, 'who', 56, 'me')

print(type(tuple_one)) #<class 'tuple'>

ages = [23, 78, 56]
ages_tuple = tuple(ages)
print(ages, type(ages), type(ages_tuple), ages_tuple)
#[23, 78, 56] <class 'list'> <class 'tuple'> (23, 78, 56)

#recommended way
tuple_two = (1,5,"yeah",42,90)
print(tuple_two)

print(tuple_two[0:2]) #(1, 5)

#fails as it does not support item assignment
#tuple_two[2] = "New Value"

A,B,C = 10,20,30
print(A, B, C)

x,y,z = [11, 334, 88]
print(x)
print(y)
print(z)

p,q,r = "Thi"
print(p, q, r)

#fails as too many values to unpack
#p,q,r = "This"

#fails as too enough values to unpack
#p,q,r = "Th"

