# Technically Blitz3.py
# Neural Network Type: Convolutional

# nn.Linear arguments:
#   in_features: size of each input sample
#   out_features: size of each output sample
#   bias: set to true by default

# nn.Conv2d arguments:
#   in_channels: Number if input channels
#   out_channels: Number of output channels
#   kernel_size: Size of convolving kernel
#   Additional Info such as the math of it is in https://pytorch.org/docs/stable/nn.html#torch.nn.Conv2d

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.conv1=nn.Conv2d(1,6,3) # 1 input Image Channel, 6 output channels and 3x3 square convoluton
        self.conv2=nn.Conv2d(6,16,3)

        #fc means Full Connection
        self.fc1=nn.Linear(16*6*6, 120)
        self.fc2=nn.Linear(120, 84)
        self.fc3=nn.Linear(84,10)
    
    def forward(self, x):
        # Convolutions -> Maxpooling -> Convolutions -> Maxpooling -> Full Connection (x3)
        x=F.max_pool2d(F.relu(self.conv1(x)),(2,2))
        x=F.max_pool2d(F.relu(self.conv2(x)), 2)
        x=x.view(-1, self.num_flat_features(x)) # Flatten Image

        x=F.relu(self.fc1(x))
        x=F.relu(self.fc2(x))
        x=self.fc3(x)
        
        return x

    def num_flat_features(self, x):
        size=x.size()[1:] # Get all dimensions excluding the batch dimension, eg: (2,2) and not (2,2,5)
        num_features=1

        for s in size:
            num_features*=s
        return num_features

net=Net()
print(net)

# Honestly at this point I didn't know what I was doing with this file

# Getting the Model Parameters
params=list(net.parameters())
print(params[0].size())

# Inputting into the Network
x=torch.randn(1,1,32,32)
out=net(x)

net.zero_grad()
out.backward(torch.randn(1,10)) # Backproping with random gradients

# Loss Function
# List Loss functions are in https://pytorch.org/docs/stable/nn.html#loss-functions

output=net(x)
target=torch.randn(10) # Random target
target=target.view(1, -1) # Since the output shape is (1,-1)
criterion=nn.MSELoss()

loss=criterion(output, target)

# Backprop
net.zero_grad()
loss.backward()

# Updating weights
# Formula for updating weights is weight = weight - learning_rate * gradient

lr=0.001

for i in net.parameters():
    i.data.sub_(i.grad.data * learning_rate)

# For training loop
optimizer=optim.SGD(net.parameters(), lr=0.001)
optimizer.zero_grad()
output=new(x)
loss=criterion(output, target)
loss.backward()
optimizer.step()
