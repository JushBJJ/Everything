x=open("asd.txt", "w")
x.write("sample ok\n")
x.write("who is joe\n joe mama")
x.close()

f=open("asd.txt")
print(f.read())

"""
or do....
for i in f:
    print(i)
"""

f.close()
