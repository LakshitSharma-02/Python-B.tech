
s1="python is a  programming language.Python is easy to learn. Python is used in AL ML"
""" 
print(s1.find("Python"))
print(s1.find("Python",35,))
print(s1.find("zython"))
print(s1.index("python"))
# print(s1.index("zython"))
print(s1.rfind("Python"))
print(s1.rfind("zython"))
print(s1.rindex("python")) 
"""

""" output="yes" if s1.find("python")!=-1 else "no"
print(output)
print(id(s1))
s2=s1.count(s1)
print(id(s1)) """


""" for i in s1:
    print(i,s1.count(i)) if s1.count(i)>2 else None """

""" for i in s1:
    print(i,s1.count(i)) if s1.count(i)>15 else None """

""" 
s3="Rajesh,Ramesh,Fazal,Kumar"
s2=s3.split(',')
print(s2,type(s2))
print(s3,type(s3))
for item in s2:
    print(item,s3.count(item))
      """


""" dob=input("enter the dob in (DD/MM/YYYY)")
year=dob.split("/")[2]
print(year)


l1=["22","12","2008"]
x="/".join(l1) """
""" 

s1="aMIT Kumar sINGh"
s2=s1.upper()
print(s1,s2)
print(s1.lower())
print(s1.capitalize())
print(s1.title())
print(s1.swapcase())

str="A12"
print(str.isupper())
print(str.isalpha())
print(str.islower())
print(str.isalnum())
print(str.isdigit())



val=input("enter a value")
val=eval(val) if val.isnumeric() else val
print(type(val)) """

name="ramesh"
age=10
place="delhi"
str1="{} is {} years oold and lives in {}".format(name,age,place)
str1="{n} is {a} years oold and lives in {p}".format(n=name,a=age,p=place)
str1=f"{name} is {age} years oold and lives in {place}"


