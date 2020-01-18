import torch.nn as NN
import torch

# Network Class Explained at QuickNotes.txt, line 11

class Perception_NN(NN.Module):
    def __init__(self):
        super(Perception_NN, self).__init__()

        self.Layer1Input=NN.Linear(3,3)
        self.Layer2Output=NN.ReLU()

    def forward(self, x):
        # x is the input
        output=self.Layer1Input(x)
        output=self.Layer2Output(x)
        return output


NN=Perception_NN()

# Feeding
x=torch.randn(1,3, dtype=torch.float)
print(NN.forward(x))
