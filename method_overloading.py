class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

# Test
calc = Calculator()
print(calc.add(5))           # Output: 5
print(calc.add(5, 10))       # Output: 15
print(calc.add(5, 10, 20))   # Output: 35
