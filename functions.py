""" def sum(a,b):
    print("The sum of two values is:", a + b)

sum(5, 10)

def concatinate(a,b):
    c=a+b
    return c

hi=concatinate("Hello ", "World")
print(hi)

def arthmetic(a,b):
    c=a+b
    d=a-b
    return c,d

x,y=arthmetic(100,78)
print(x)
print(y)

def m1():
    print("This is m1 function")
def m2():
    print("This is m2 function")
    m1()
m2() """


""" 
functions are considiered as first-class objects. In python, below things are possible to

1.assign a function to a variable
2.pass a function as a parameter to another function
3.define a function inside another function
4.the function can return another function
 """
""" 
#1.Assigning a function to a variable
def add():
    print("This is add function")
sum=add
sum()


#2. Passing a function as a parameter to another function
def message(func):
    print(func)

def printmessage(x):
    x("Hello World")

printmessage(printmessage)
 """

""" 
a=int(input("Enter a number:"))
if 0<a<10:
    print("The number is between 0 and 10")
else:
    print("none of the above")
"""
""" 
def add(x,y):
    return x+y
sum=add
print(sum(12,5))
 """

""" 
# Passing a function as argument to another function
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def operate(func,a,b):
    return func(a,b)
print(operate(add,10,5))
print(operate(sub,12,5))
 """

""" 
#function can be defined inside another function....
def outer():
    print("This is outer function")
    def inner():
        print("This is inner function")
    inner()

outer()


 """
""" 
# function can return another function
def outer():
    print("outside function")
    def inner():
        print("inside function")
    return inner

func1=outer()
func1()
 """

""" 
def createfunction():
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    return add,sub
def executefunction(func,a,b):
    return func(a,b)
add_func,sub_func=createfunction()
print(executefunction(add_func,10,5))
print(executefunction(sub_func,10,5))
 """
""" 
def add(x,y):
    return x+y
l=[add,23,26]
val=l[0](l[1],l[2])
print(val)

l=[add,len]
for f in l:
    print(f([1,2,3,4,5]))
"""


""" 
# positional arguments
def details(name,age):
    print("Name:", name)
    print("Age:", age)

details("Alice", 25)
details(34,"amit")

# keyword arguments
details(age=30,name="Suresh")

# default arguments
def simpleinterest(p,r=2.5,t=2):
    return(p*t*r)/100

print(simpleinterest(1000))
print(simpleinterest(1000,3,5))
print(simpleinterest(1000,3.5,5))
 """
""" 
def add(x,*y):
    print(type(y))
    total=x
    for i in y:
        total+=i
    return total
print(add(12,45,78))
print(add(2,3,4,5,6,7,8,9,5))
print(add(2,6,7))
print(add(10))
print(add(10,))
print(add()) """

""" 
def add(*y):
    print(type(y))
    total=0
    for i in y:
        total+=i
    return total
print(add(12,45,78))
print(add(2,3,4,5,6,7,8,9,5))
print(add(2,6,7))
print(add(10))
print(add(10,))
print(add())
 """
""" 
def m():
    a=10
    print(a)
def n():
    print(a)
m()
n()
"""
""" 

a=11
b=12
def m1():
    print(a)
    print(b)
def m2():
    print(a)
    print(b)
    
m1()
m2()
"""  """
a=1
def m1():
    a=2
    print(a)
def m2():
    print(a)

def m3():
    global a
    a=3
    print(a)
m1()
m2()
m3()

print(a)
 """

""" a=1
def m1():
    a=2
    print(a)
    print(globals()['a'])
m1() """

""" x=1
while x!=11:
    print(x)
    x+=1 """

""" 
# x=11
def num(n):
    if n>10:
        return
    print(n)
    num(n+1)

num(1)

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
fact=factorial(5)
print(fact)


def power(x,y):
    if y==0:
        return 1
    else:
        return x*power(x,y-1)
pow=power(2,3)
print(pow)

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
fib=fibonacci(5)
print(fib)
"""
""" 
def sod(n):   #sum of digits
    if n=="":
        return 0
    else:
        return int(n[0])+sod(n[1:])
print(sod("12345"))


def sumofdigits(num):
    if num==0:
        return 0
    else:
        return num%10 + sumofdigits(num//10)
print(sumofdigits(1234567)) """

""" def reversed(s1,s2):
    if s1=="":
        return s2
    else:
        return (s2+s1[-1]) + reversed(s1[:-1],s2)

print(reversed("hey","")) """


""" def reversed(num1,num2):
    if num1==0:
        return num2
    else:
        return (num2+num1%10) + reversed(num1//10,num2)

print(reversed(12345,0)) """
""" 
def apnamap(f,l):
    for i in l:
        yield f(i)
l=[1,2,3,4,5]
l=list(apnamap(str,l))

s=list(apnamap(int,input().split()))
print(s) """
""" 
def m(x,y):
    while x<=y:
        yield x
        x+=1
g=m(5,10)
print(type(g))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
 """
from functools import reduce
m,n=map(int,input().split())

matrix=[list(map(int, input().split())) for _ in range(m)]

row_sum=list(map(sum,matrix))
col_sum=list(map(sum,zip(*matrix)))

max_sum=max(row_sum)
max_row=row_sum.index(max_sum)+1

total=reduce(lambda x,y:x+y,row_sum)

print("row sum:",row_sum)
print("col sum:",col_sum)
print("max_row:",max_row)
print("total:",total)