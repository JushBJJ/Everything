import torch
import torch.nn as nn
import torch.nn.functional as f
import torch.optim as opt

import numpy as np

from matplotlib import pyplot as plt 
from math import exp

class network(nn.Module):
	def __init__(self):
		super(network, self).__init__()		

		self.layer1=nn.Linear(3,6)
		self.layer2=nn.Linear(6,3)
		self.layer3=nn.Linear(3,1)
		
		self.activation=nn.Sigmoid()

	def forward(self, x, desired_outputs):
		x=self.activation(self.layer1(x))
		x=self.activation(self.layer2(x))
		x=self.activation(self.layer3(x))
		
		return x
net=network()
x=torch.tensor([[1.,1.,1.],[0.,1.,0.],[0.,0.,1.],[1.,0.,1.]], requires_grad=True)
desired=torch.tensor([[1.],[0.],[0.],[1.]])

print("Inputs: ", x)
print("Network: ", net)
print("desired: ", desired)

lossfn=nn.MSELoss()
optimizer=opt.SGD(net.parameters(), lr=0.0001)
epochs=100000

losses=torch.zeros(epochs)

checkpoint=0

for epoch in range(epochs):
	out=net.forward(x, desired_outputs=desired)
	
	optimizer.zero_grad()
	loss=lossfn(out, desired)
	loss.backward()
	losses[epoch]=loss	
	
	print("Epoch: {}\tLoss: {}".format(epoch, loss))
	
	optimizer.step()


plt.title("Neural Network Loss: Sigmoid")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.plot(losses.detach().numpy())
plt.show()
