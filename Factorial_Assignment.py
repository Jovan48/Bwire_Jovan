# use lamba program to find factorial of a number

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
num = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {num} is {factorial(num)}")        