""" 
#print(10/0) #ZeroDivisionError
print("One")
print("Two")
try:
    print(10/0)
except ZeroDivisionError:
    print("exceptionpassed")
print("four")
print("five")
 """
"""
print("One")
print("Two")
try:
    print(10/0)
except ZeroDivisionError as z:
    print("exception informmation:",z)
print("four")
print("five")
"""
""" 
try:
    x=int(input("enter a number:"))
    y=int(input("enter a number:"))
    print(x/y)
except ZeroDivisionError:
    print("cant divide with zero")
except ValueError:
    print("please provide int value only")
 """


try:
    x=int(input("enter a number:"))
    y=int(input("enter a number:"))
    print(x/y)
except (ZeroDivisionError,ValueError) as  e:
    print("please provide valid nnumbers and problem is :", e)
except:
    print("default except: please proviide valid input only")
finally:
    print("finally balock")