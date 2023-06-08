# x = "This is the variable"
# print(x)
# print(id(x))

# first = "Krishna"
# last = "Regmi"
# print(first,last) #Krishna Regmi
# print(first+last) #KrishnaRegmi

# x = 5
# y = "Krishna"
# print(x+y) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Global variable concept
# name = "Krishna"

# def myfun():
#     print("Hello "+name)

# myfun()

#Another example
# name = "Krishna"

# def myfun():
#     name = "Kushal"
#     print("Hello "+name)

# myfun()

# print("Hello "+name)

#The global Keyword
#If you use the global keyword, the variable belongs to the global scope
# def myfun():
#     global name
#     name = "Krishna"

# myfun()

# print("Hello "+name)

#Another example
# name = "Krishna"

# def myfun():
#     global name
#     name = "Kushal"

# myfun()

# print("Hello "+name)

#Getting the Data Type
# x = 5
# print(type(x))
# x = 5 + 2j
# print(type(x))