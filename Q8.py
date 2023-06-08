import functools
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = functools.reduce(lambda x,y: x+y, [10,23, -45, 33])
A8 = map(lambda x: x*2, [1,2,3,4])
A9 = filter(lambda x: len(x) >3, ["I" , "want", "to", "learn", "python"])
print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)
print(A7)
print(A8)
print(A9)

# Explaine the output of A0
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(A0)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Using zip() function we can map the similar index of multiple containers so that they can be used just using as single entity. and dict() function is used to create a dictionary. so that the output is a dictionary with keys as 'a','b','c','d','e' and values as 1,2,3,4,5 respectively.

# Explaine the output of A1
A1 = range(10)
print(A1)
# Output: range(0, 10)
# range() function is used to generate a sequence of numbers. so that the output is a sequence of numbers from 0 to 9. 

# Explaine the output of A2
A2 = sorted([i for i in A1 if i in A0])
print(A2)