from __future__ import print_function
import torch

# Autograd: Automatic differentiation

x=torch.ones(2,2, requires_grad=True)
y=x+2

print("y autogradient function: ", y.grad_fn)
z=y*y*3
out=z.mean()
print("out value: ", out)

# Enabling autograd on existing tensors
a=torch.randn(5,3)
a=((a*3)/(a-1))
print("a requires grad: ", a.requires_grad)
a.requires_grad_(True)
print("a requires grad: ", a.requires_grad)
b=(a*a).sum()
print("b autograd function: ", b.grad_fn)

# Backpropagating (Math is explained in https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html)
out.backward()
print("x value: ", x)
print("x gradient: ", x.grad)

# Vector Jacobian product
x=torch.randn(3, requires_grad=True)

y=x*2
while y.data.norm() < 1000:
    y=y*2

print("y when using jacobian product: ", y)

# Stopping autograd from tracking history on tensors that has requires_grad=True
with torch.no_grad():
    print((x**2).requires_grad)
# Or do y=x.detach() but the code last 2 lines disables autograd for all tensors
