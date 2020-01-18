# Lines explained at QuickNotes.txt at line 37

import torch
import torch.nn as nn

class FFN(nn.Module):
    def __init__(self):
        super(FFN, self).__init__()

        self.l1=nn.Linear(3,6)
        self.l2=nn.Linear(6,3)
        self.l3=nn.Linear(3,2)
        self.l4=nn.Softmax(dim=-1)
        self.Activation=nn.ReLU()

    def forward(self, x):
        # Layer 1
        seq=self.l1(x)
        seq=self.Activation(seq)
        seq=self.l2(seq)
        seq=self.Activation(seq)
        seq=self.l3(seq)

        # Change shape to [x, 1]
        seq.view(x.shape[0],2)

        seq=self.l4(seq)

        return seq
    
# Sample
x=torch.Tensor([[0,0,1],[1,1,1],[1,0,0], [0,1,0],[1,0,1]])

# Network
Net=FFN()
out=Net.forward(x)
print(out)
