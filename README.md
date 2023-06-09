# Problem 1
```python
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr
```

# Problem 2
```python
def file_type(ext_type, file_list):
    ext_type = ext_type.split(';')
    ext_type = [i.split(',') for i in ext_type]
    ext_type = dict(ext_type)
    file_type = {}
    for i in file_list:
        if i.split('.')[-1] in ext_type.keys():
            file_type[i] = ext_type[i.split('.')[-1]]
        else:
            file_type[i] = 'unknown'
    return file_type
```

# Problem 3
```python
def sort_list_of_dict(list_of_dict, key):
    return sorted(list_of_dict, key=lambda x: x[key])
```

# Problem 4
```python
def switch_key_value(d):
    return {v: k for k, v in d.items()}
```

# Problem 5
```python
def f(mainstream, must_watch):
    common = list(set(mainstream) & set(must_watch))
    uncommon = list(set(mainstream) ^ set(must_watch))
    return common, uncommon
```

# Problem 6
```python
def f(arr, start, end):
    return arr[start:end:2]
```

# Problem 7
```python
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
```

# Problem 8
```python
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
```
#### Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#### Using zip() function we can map the similar index of multiple containers so that they can be used just using as single entity. and dict() function is used to create a dictionary. so that the output is a dictionary with keys as 'a','b','c','d','e' and values as 1,2,3,4,5 respectively.
```python
A1 = range(10)
```
#### Output: range(0, 10)
#### range() function is used to generate a sequence of numbers. so that the output is a sequence of numbers from 0 to 9. 
```python
A2 = sorted([i for i in A1 if i in A0])
```
#### Output: []
#### sorted() function is used to sort the elements of a given iterable in a specific order. In this case it itartes in the range of 0 to 9 and checks if the number is are key in the dictionary A0. if it is in the dictionary then it is appended to the list and then it sort the list. but in this case the dictionary A0 does not have any keys in the range of 0 to 9. so the output is an empty list. but if have the keys in the between 0 to 9 then the output is a sorted list of keys.

#### The above code is equivalent to:
```python
A2 = []
for i in A1:
    if i in A0:
        A2.append(i)
A2 = sorted(A2)
```

```python
A3 = sorted([A0[s] for s in A0])
```
#### Output: [1, 2, 3, 4, 5]
#### sorted() function is used to sort the elements of a given iterable in a specific order. In this case it itartes in the dictionary A0 and save the values (A0[s]) in a list and then it sort the list. so the output is a sorted list of values of the dictionary A0.

#### The above code is equivalent to:
```python
A3 = []
for s in A0:
    A3.append(A0[s])
A3 = sorted(A3)
```

```python
A4 = [i for i in A1 if i in A3]
```
#### Output: [1, 2, 3, 4, 5]
#### In this case it itartes in the range of 0 to 9 and checks if the number is are in the list A3. if it is in the list then it is appended to the list. so the output is a list of numbers from 0 to 9.

#### The above code is equivalent to:
```python
A4 = []
for i in A1:
    if i in A3:
        A4.append(i)
```

```python
A5 = {i:i*i for i in A1}
```
#### Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
#### In this case it itartes in the range of 0 to 9 and creates a dictionary with keys as the numbers from 0 to 9 and values as the square of the numbers. so the output is a dictionary with keys as 0,1,2,3,4,5,6,7,8,9 and values as 0,1,4,9,16,25,36,49,64,81 respectively.

#### The above code is equivalent to:
```python
A5 = {}
for i in A1:
    A5[i] = i*i
```

```python
A6 = [[i,i*i] for i in A1]
```
#### Output: [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
#### In this case it itartes in the range of 0 to 9 and creates a list of lists with the first element of the list as the number from 0 to 9 and the second element of the list as the square of the number. so the output is a list of lists with the first element of the list as 0,1,2,3,4,5,6,7,8,9 and the second element of the list as 0,1,4,9,16,25,36,49,64,81 respectively.

#### The above code is equivalent to:
```python
A6 = []
for i in A1:
    A6.append([i,i*i])
```

```python
A7 = functools.reduce(lambda x,y: x+y, [10,23, -45, 33])
```
#### Output: 21
#### functools.reduce() function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. so in this case it adds all the elements of the list. so the output is 21.

#### The above code is equivalent to:
```python
A7 = 0
for i in [10,23, -45, 33]:
    A7 += i
```

```python
A8 = map(lambda x: x*2, [1,2,3,4])
```
#### Output of list(A8): [2, 4, 6, 8]
#### map() function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. In this case it multiplies all the elements of the list by 2. so the output is a map object with the elements of the list multiplied by 2.

```python
A9 = filter(lambda x: len(x) >3, ["I" , "want", "to", "learn", "python"])
```
#### Output of list(A9): ['want', 'learn', 'python']
#### filter() function is used to filter the given iterable with the help of another function passed as an argument to test all the elements to be True or False. In this case it filters the list with the length of the elements greater than 3. so the output is a filter object with the elements of the list with length greater than 3.

# Problem 9
```python
from datetime import datetime
from datetime import timedelta
def date_diff(from_date, to_date, difference):
    from_date = datetime.strptime(from_date, '%y-%m-%d')
    to_date = datetime.strptime(to_date, '%y-%m-%d')
    if (to_date - from_date) < timedelta(days=difference):
        return True
    else:
        return False
```

# Problem 10
```python
from datetime import datetime
from datetime import timedelta
def f(date, n):
    from_date = datetime.strptime(date, '%y-%m-%d')
    to_date = from_date - timedelta(days=n)
    return to_date.strftime('%y-%m-%d')
```