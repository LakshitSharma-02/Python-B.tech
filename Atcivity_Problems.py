# 1
""" 
str1=input("enter a string :")
Even_pos=str1[0::2]
Odd_pos=str1[1::2]
print("Even positions:",Even_pos)
print("Odd positions:",Odd_pos)
"""


# 1

""" 
x=int(input("enter a number"))
if x<0:
    print("The number is negative")
else:
    print("The no is positive")

 """


""" 
# 2
user_name="rahul"
x=input("enter a number")
if  user_name.upper()==x.upper():
    print("The name is valid")
else:
    print("The  name is invalid")

 """

""" 
# 3
x=int(input("Enter First Number"))
y=int(input("Enter Second Number"))
if x<y:
    print("Biggest Nummber is :", x)
else:
    print("Biggest Number is :", y)
 """
""" 
# 4
English_marks=int(input("enter english marks"))
Hindi_marks=int(input("enter hindi marks"))
Maths_marks=int(input("enter Maths marks"))
Science_marks=int(input("enter Science marks"))
Geography_marks=int(input("enter Geography marks"))
History_marks=int(input("enter History marks"))
sum=English_marks + Hindi_marks + Maths_marks + Science_marks + Geography_marks + History_marks 
Avg=sum/6
if Avg<=100 and Avg>=90:
    print("A+")
    print("Ramu has PASSED")
elif Avg<=89 and Avg>=80:
    print("A")
    print("Ramu has PASSED")
elif Avg<=79 and Avg>=70:
    print("B+")
    print("Ramu has PASSED")
elif Avg<=69 and Avg>=60:
    print("B")
    print("Ramu has PASSED")
elif Avg<=59 and Avg>=45:
    print("c")
    print("Ramu has PASSED")
elif Avg<=44 and Avg>=33:
    print("D")
    print("Ramu has PASSED")
else:
    print("Fail")
    print("Ramu has FAILED")

 """

""" 


x=[1,2,3,4,5,"python"]
for i in x:
    print(i)

x="python"
for ch in x:
    print(ch)
item_costs=[10,20,30]
gst=2
for x in item_costs:
    print(x+gst)
for x in range (1,5):
    print(x)


 """

""" 

item_costs=[10,20,30]
sum=0
for x in item_costs:
    sum+=x
print(sum)


 """
""" 
Num=int(input("enter the number:"))
New_Num=str(Num)
sum=0
for i in Num:
    sum=sum+int(i)
print("sum of the digits is",sum)

 """
""" 
# 2
str1=str(input("enter a string:"))
start=eval(input("Enter start index : "))
end=eval(input("Enter end index :"))
print("Original string is ", str1)
print("Substring :",str1[start:end])
print("Reversed substring :", str1[end-1:start-1:-1])

 """


""" 
# 3
str1=str(input("Enter a string :"))
Rev_str1=str1[::-1]
if str1==Rev_str1:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

 """""" 

str1=str(input("enter a string :"))
print("Original :",str1[:])
print("First 3:", str1[:3])
print("Last 3:", str1[-3::1])
print("Index 2 to 7 :", str1[2:8])
print("Every 2nd character :", str1[::2])
print("Reversed", str1[::-1])

 """
""" 
str1=str(input("enter email :"))
# lakshit.sharma@gmail.com
str1_ind=str1.find("@")
if str1_ind !=-1:
    print("User domain",str1[:str1_ind])
    print("company domain",str1[str1_ind:])
else:
    print("invalid email")

 """


