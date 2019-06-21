# https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/01-basics/pytorch_basics/main.py

import torch
import torchvision
import torch.nn as nn
import numpy as np
import torchvision.transforms as transforms

# ================================================================== #
#                     1. Basic autograd example 1                    #
# ================================================================== #
x = torch.tensor(1.,requires_grad=True)
w = torch.tensor(2.,requires_grad=True)
b = torch.tensor(3.,requires_grad=True)

y= w*x+b
y.backward()
print(x.grad)
print(w.grad)
print(b.grad)

# ================================================================== #
#                    2. Basic autograd example 2                     #
# ================================================================== #
x = torch.randn(10,3)
y = torch.randn(10,2)

linear = nn.Linear(3,2)
print('w:',linear.weight)
print('b:',linear.bias)

##build loss function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(),lr=0.01)

## forward pass
pred = linear(x)

## compute loss
loss = criterion(pred,y)
print('loss:', loss.item())

# Backward pass
loss.backward()

##print out the gradients
print('dL/dw:',linear.weight.grad)
print('dL/db:',linear.bias.grad)

##1-step gradient descent
optimizer.step()

#print out the loss after 1-step gradient descent
pred = linear(x)
loss = criterion(pred,y)
print('loss after 1 step optimization:',loss.item())

