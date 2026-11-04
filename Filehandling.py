""" 
f=open("abc.txt","w")
print("file name:",f.name)
print("file mode:",f.mode)
print("file readable:",f.readable())
print("file writable:",f.writable())
print("file closed:",f.closed)
f.close()
print("file closed:",f.closed)
"""


"""
f=open("wish.txt","w")
f.write("welcome\n")
f.write("to\n")
f.write("python World\n")
print("Data written successfully")
f.close()
"""

f=open("wish.txt","a")
f.write("welcome\n")
f.write("to\n")
f.write("python World\n")
print("Data written successfully")
f.close()