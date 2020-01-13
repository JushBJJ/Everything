from __future__ import print_function
import torch
import numpy as np

#===============================#
print("Types of Tensors: \n")
# Unintialized Tensor
x=torch.empty(5,3)
print("\nEmpty Uninitialized Tensor: \n", x)

# Random Tensor
x=torch.rand(5,3)
print("\nRandom Tensor: \n", x)

# Empty Initialized Tensor
x=torch.zeros(5,3)
print("\nEmpty Initialized Tensor: \n", x)

# Creating a Tensor out of an existing tensor
x=x.new_ones(5,3, dtype=torch.double) # Initialized Tensor filled with onesa
print("\nInitialized Tensor filled with 1s: \n", x)

y=torch.rand_like(x, dtype=torch.float)
print("\nTensor filled with random numbers with overrided data type using the same tensor as \'x\': \n", y)

print("\nSize of x: {}\n Size of y: {}\n".format(x.size(), y.size()))


#===============================#
# Incrementing

print("Incrementing: \n")
x=x.new_ones(5,3) # Filled with 1s
y=y.new_ones(5,3) # Filled with 1s

# Just like 1+1

# Method 1
print("\nx+y=", x+y)

# Method 2
print("\nx+y=", torch.add(x,y)) # Personally I would choose this but I please feel free to disprove me. And I would likely reconsider.

# Adding the sum of x and y into a new tensor variable
z=torch.empty(5,3)
torch.add(x,y, out=z)
print("Z: ", z)

# Incrementing Tensor variable
z=z.add_(x)
print("Z incremented: ", z)

#===============================#
# Index Slicing
z=torch.rand(5,3, dtype=torch.float)
print("Index slicing: \n")
print(z[:3])
print(z[:,1])
print(z[:1,1])

#===============================#
# Resizing/Reshaping Tensors
print("Reshaping tensors: \n")
print("z shape: ", z.shape)

z=z.view(15)
print("New z shape: ", z.shape)

#===============================#
# When the tensor only has 1 value you can get that value as a python number
x=torch.rand(1) # tensor([[1]])
print(x.item())

#===============================#
# Numpy Bridge (Converting from Numpy to Torch Tensor or Torch Tensor to Numpy)
print("\nNumpy Bridge: \n")

# Converting from Torch Tensor to Numpy
x=torch.ones(5)
y=x.numpy()
print("Comparing x (pytorch tensor) and y (numpy ndarray) conversion: \n{}, {}".format(x,y))

# Converting from Numpy to Torch Tensor
x=np.ones(5)
a=torch.from_numpy(x)
print("\nNumpy array(x): ", x, "\nConverted from Numpy to Torch Tensor: ", a)
