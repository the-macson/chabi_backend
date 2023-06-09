import functools

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Using zip() function we can map the similar index of multiple containers so that they can be used just using as single entity. and dict() function is used to create a dictionary. so that the output is a dictionary with keys as 'a','b','c','d','e' and values as 1,2,3,4,5 respectively.

A1 = range(10)
# Output: range(0, 10)
# range() function is used to generate a sequence of numbers. so that the output is a sequence of numbers from 0 to 9. 


A2 = sorted([i for i in A1 if i in A0])
# Output: []
# sorted() function is used to sort the elements of a given iterable in a specific order. In this case it itartes in the range of 0 to 9 and checks if the number is are key in the dictionary A0. if it is in the dictionary then it is appended to the list and then it sort the list. but in this case the dictionary A0 does not have any keys in the range of 0 to 9. so the output is an empty list. but if have the keys in the between 0 to 9 then the output is a sorted list of keys.

# The above code is equivalent to:
A2 = []
for i in A1:
    if i in A0:
        A2.append(i)
A2 = sorted(A2)


A3 = sorted([A0[s] for s in A0])
# Output: [1, 2, 3, 4, 5]
# sorted() function is used to sort the elements of a given iterable in a specific order. In this case it itartes in the dictionary A0 and save the values (A0[s]) in a list and then it sort the list. so the output is a sorted list of values of the dictionary A0.

# The above code is equivalent to:
A3 = []
for s in A0:
    A3.append(A0[s])
A3 = sorted(A3)


A4 = [i for i in A1 if i in A3]
# Output: [1, 2, 3, 4, 5]
# In this case it itartes in the range of 0 to 9 and checks if the number is are in the list A3. if it is in the list then it is appended to the list. so the output is a list of numbers from 0 to 9.

# The above code is equivalent to:
A4 = []
for i in A1:
    if i in A3:
        A4.append(i)


A5 = {i:i*i for i in A1}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# In this case it itartes in the range of 0 to 9 and creates a dictionary with keys as the numbers from 0 to 9 and values as the square of the numbers. so the output is a dictionary with keys as 0,1,2,3,4,5,6,7,8,9 and values as 0,1,4,9,16,25,36,49,64,81 respectively.

# The above code is equivalent to:
A5 = {}
for i in A1:
    A5[i] = i*i


A6 = [[i,i*i] for i in A1]
# Output: [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
# In this case it itartes in the range of 0 to 9 and creates a list of lists with the first element of the list as the number from 0 to 9 and the second element of the list as the square of the number. so the output is a list of lists with the first element of the list as 0,1,2,3,4,5,6,7,8,9 and the second element of the list as 0,1,4,9,16,25,36,49,64,81 respectively.

# The above code is equivalent to:
A6 = []
for i in A1:
    A6.append([i,i*i])


A7 = functools.reduce(lambda x,y: x+y, [10,23, -45, 33])
# Output: 21
# functools.reduce() function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. In this case it adds all the elements of the list. so the output is the sum of all the elements of the list.

# The above code is equivalent to:
A7 = 0
for i in [10,23, -45, 33]:
    A7 += i


A8 = map(lambda x: x*2, [1,2,3,4])
# Output of list(A8): [2, 4, 6, 8]
# map() function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. In this case it multiplies all the elements of the list by 2. so the output is a map object with the elements of the list multiplied by 2.


A9 = filter(lambda x: len(x) >3, ["I" , "want", "to", "learn", "python"])
# Output: ['want', 'learn', 'python']
# filter() function is used to select some particular elements from a sequence of elements. In this case it checks if the length of the element is greater than 3. if it is greater than 3 then it is appended to the list. so the output is a filter object with the elements of the list with length greater than 3.

