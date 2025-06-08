# write a program to handle errors, the program should ask for two numbers using input and divide them
# use an infinite loop to keep asking for input until the user enters valid numbers
def divide_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
            print(f"The result of dividing {num1} by {num2} is {result}")
            break  
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a non-zero second number.")     
            
divide_numbers()    