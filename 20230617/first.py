#Work on try and except block

# x = 5
# y = "Hello World"

# z = x + y # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print(z)
#--------------------------------------------------------------------------
# try:
#     x = 5
#     y = "Hello World"

#     z = x + y

# except TypeError:
#     print("Can't be possible to add integer and string value.")

#--------------------------------------------------------------------------
try:
    x = 5
    y = "Hello World"

    z = x + y

except:
    print("Can't be possible to add integer and string value.")
