first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

try :
    result = first / second
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    exit()
print("Result is ",result)