# While loop

print("While Loop\n============\n")

x = 0
while(x<10):
    x+=1
    print(x)

# For loop
print("\nFor loop\n============\n")
for i in range(10):
    print(i)

# For loop arrays
print("\nFor loop array\n============\n")
x=[1,2,3,4,5,"asd", "hello"]

for i in x:
    print(i)

print("or....")
for i,j in enumerate(x):
    z="{x}: {y}".format(x=i, y=j)
    print(z)
