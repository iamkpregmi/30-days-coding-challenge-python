#except and else

# def myfun(a,b):
    
#     try:
#         c = a / b
    
#     except ZeroDivisionError:
#         print("Cannot possible to divide by zero.")
#     else:
#         print(c)  #execute only when except block not execute
# myfun(10,0)

# #-------------------------------------------------------------------------
# #multiple except
# try:
#     first = int(input("Enter first number: "))
#     second = int(input("Enter second number: "))
    
#     result = first / second

# except ZeroDivisionError:
#     print("Cannot possible to divide by zero.")
# except ValueError:
#     print("Input must be integer and float value only.")
# else:
#     print("Result is: ",result)

#-------------------------------------------------------------------------
#Finally keyword in exception
try:
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    
    result = first / second

except ZeroDivisionError:
    print("Cannot possible to divide by zero.")
except ValueError:
    print("Input must be integer and float value only.")
else:
    print("Result is: ",result)
finally:
    print("this is the end of code") #it's code execute every time