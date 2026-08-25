#--Logical  operators--

from sys import argv

val=(12 and 5)-3
#print(val)
val=("abcd" and "trs")
#print(val)
'''
print(0 and 4)
print(5 and 7)
print(21 and 0)
print(15 and 9)
'''

'''
print(0  or 4)
print(5 or 7)
print(2 or 0)
print(15 or 9)
'''

'''
print(not 4)
print(not 0)
'''

'''
x=19
y=4
x+=y
y-=x
print(x)
print(y)
x//=y
print(x)
x*=y
print(x)
x**=y
print(x)
'''

'''
x=10
print(x)
print(-x)
'''

'''
text="Welcome to python programming"
print("Welcome" in text)
print("hello" in text)
print("python " in text)
print("hari " not in text)
'''


'''
a=25
b=25
c=60
'''

'''
print(id(a))
print(id(b))
print(id(c))
'''

'''
print(a is b)
print(a is c)
print(a is not c)
'''


'''
x=str(input("enter your name:"))
print("you entered name as :", x)
'''

'''
a=int(input("enter a no"))
b=int(input("enter 2nd no."))
print("sum is:", a+b)
'''


'''
p=int(input("enter principle amt:"))
r=float(input("enter interest :"))
t=float(input("enter time in yrs :"))
simple_interest=(p*r*t)/100
print("simple interest is :", simple_interest)
'''

# print(eval("10 + 10"))
# print(eval("10/10"))
# print(eval("10//10"))
# print(eval("10*10"))
# print(eval("10**10"))
# print(eval("10 - 10"))

# for i in range (4):
#     val=eval(input("enter a value :"))
#     print(val)
#     print(type(val))

a=eval(argv[1])
b=eval(argv[2])
c=a+b
print(c)


