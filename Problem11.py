def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)

# output of f(2) is [0,1] because the list l is empty and the for loop runs for 2 times and the values are appended to the list l. when i = 0, l = [0] and when i = 1, l = [0,1]. so the output is [0,1].

# output of f(3,[3,2,1]) is [3,2,1,0,1,4] because the list l is [3,2,1] and the for loop runs for 3 times and the values are appended to the list l. when i = 0, l = [3,2,1,0] and when i = 1, l = [3,2,1,0,1] and when i = 2, l = [3,2,1,0,1,4]. so the output is [3,2,1,0,1,4].

# output of f(3) is [0,1,4] because the list l is [0,1,4] and the for loop runs for 3 times and the values are appended to the list l. when i = 0, l = [0,1,4,0] and when i = 1, l = [0,1,4,0,1] and when i = 2, l = [0,1,4,0,1,4]. so the output is [0,1,4].

# At every iteration, the value of i*i is appended to the list l. if l is emepty then the value for f(n) is [0,1,4,9,......,n*n] and if l is not empty then the value for f(n,l) is [l[0],l[1],l[2],l[3],......,l[n-1], 0,1,4,9,......,n*n].