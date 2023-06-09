factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

num = 6
result = factorial(num)

print(f"The factorial of {num} is: {result}")
