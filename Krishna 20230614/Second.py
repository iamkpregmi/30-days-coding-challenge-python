try :
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))    
    result = first / second
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    exit()
except ValueError:
    print("Error: Input must be integer try again...")
    exit()
print("Result is ",result)