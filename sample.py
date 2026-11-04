""" name=input("enter your age")
age=int(input("enter you age"))
city=input("enter your city")
print("hello {}, you are {} years old and live in {}".format(name,age,city)) """

""" 
str1=input("")
print(str1[::-1])
count=0
for i in str1:
    if i in "aeiouAEOIU":
        count+=1
str2=str1.replace(" ","_")
print(count)
print(str2) """

""" 
l1=tuple(map(int,input("").split()))
a,b=l1
print("before swapping: a={}, b={}".format(a,b))
b,a=a,b
print("after swapping: a={}, b={}".format(a,b)"""


l1=list(map(int,input("").split()))
l2=list(map(int,input("").split()))
s1=set(l1)
s2=set(l2)
print(s1 & s2)
print(list(map(lambda x:x**2 for i in range(1,20))))