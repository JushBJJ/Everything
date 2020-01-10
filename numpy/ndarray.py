import numpy as np

foo=np.array([1,2,3])
print(foo)

for i in foo:
    print(i)

foo=np.array([[1],[2],[3]])

for i in foo:
    for x in i:
        print(x)
