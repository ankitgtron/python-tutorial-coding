x = input("Enter number1: ")
y = input("Enter number2: ")
try:
    z = int(x)/ int(y)
except ZeroDivisionError as e:
    print("Exception ZeroDivisionError")
    z=None
except TypeError as e:
    print("Exception TypeError")
    z = None
print("Division is: ", z)

