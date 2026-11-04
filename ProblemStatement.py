""" # Problem statement 1
""" 
str1=str(input("Enter a string :"))
New_str=""
str2=str1.split(" ")
print(str2)
for i in range (0,len(str2)):
    New_str+=str2[i][0::2]+" "
print(New_str) """

# problem state 2
""" 
str1=input("enter a string :")
sub_str=input("enter a substring :")
print(str1.count(sub_str))

 """

# Problem statement 3
""" 
step1-Enter a string
step2-creater a empty string
step3-loop through every character
        a-check  whether the char count should be greater thand one and should not repeated in the new string
        b-conact it with the new string 
step4-print new strinng
"""

""" str1=input("enter a string:")
sub=""
for i in range(len(str1)):
    if(str1.count(str1[i])!=0 and str1[i] not in sub) :
        sub+=str1[i]+str(str1.count(str1[i]))+" "
print(sub.strip()) """


str1=input("enter a string consisting only of * and # :")
sum1=str1.count("*")
sum2=str1.count("#")
if sum1>sum2:
    print(sum1-sum2,"number of * is greater than #")
elif sum1<sum2:
    print(sum1-sum2,"number of # is greater than *")
else:
    print(0,"number of * and # are equal")



 """