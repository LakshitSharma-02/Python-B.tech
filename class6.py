from sys import argv
# print("Hello, World!")
'''
print(argv[0])
print(argv[1])
print(argv[2])
'''
# a=eval(argv[1])
# b=eval(argv[2])
# c=a+b
# print(c)

# print("the length of values:",len(argv))
""" 
str1="Rajeev's Diary"
str2='rajeev said "i am a good boy"'
print(str1)
print(str2)
 """

""" 
c=""+34-4
print(c) 
"""
""" 
c=bool("")+34-4
print(c) 


c=bool("hi")+34-4
print(c) 

 """


# indexing and slicing


"""
print(str[0])
print(str[len(str)-1])
print(str[-1])
print(str[-len(str)])
for c in range(len(str)):
    print(str[c])
 """

""" 
str1="rajeev"
for i in range(-len(str1),0):
    print(str1[i])

for i in range(len(str1)):
    print(str1[i])

for i in str1:
    print(i)

 """

""" 
str1="python in GLA CL2"
print(str1[::])
print(str1[2:6:2])
print(str1[10:13:1])
print(str1[13:9:-1])
print(str1[-5:9:1])

"""

""" 
name="rajeev"
print(name)
print(name[0])
name[0]="y"
 """
""" 
str1="python"
str2="programming"
str3=3
print(str1+str2+str3)
print(str1+str2)
print(str1*3)
#checking membership operator
print("thon" in str1)
print("thon" not in str1)
print("thon" in str2)
print("thon" not in str2)
print('e' in str1)
 """

""" 
s1='abcd'
s2='abcdefg'
print(s1==s2)
if s1==s2:
    print("both are equal")
else:
    print("both are not equal")
 """


""" 
s1='abcd'
s2='abcdefg'
output=print(s1==s2) if s1==s2 else print("both are not equal")
print(output)
output= "same" if s1==s2 else "not same"
print(output)
"""
s1="Amit Singh"
print(len(s1))
print(s1.strip())