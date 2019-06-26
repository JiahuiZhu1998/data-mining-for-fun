# https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/01-basics/pytorch_basics/main.py
# https://blog.csdn.net/jacke121/article/details/80772627
# 6/20/2019
# part 4 need to connect to torondo university to get dataset,so I cannot finish part 4-7 when I am working in Nanjing
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
x = torch.randn(10,3)## 3d data,number of data is ten
y = torch.randn(10,2)## 2d data number of data is ten
print('\n')
linear = nn.Linear(3,2)##in_features=3,out_features=2,bias=True

# tensor([[-0.5578,  0.3046, -0.5394],
#         [-0.1954,  0.3101,  0.1928]], requires_grad=True)
print('w:',linear.weight)
# b: Parameter containing:
# tensor([0.1531, 0.4510], requires_grad=True)
print('b:',linear.bias)
print('\n')

##build loss function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(),lr=0.01)
## forward pass
pred = linear(x) ## x is 3d data
print(pred) ##pred is y in general

## compute loss
loss = criterion(pred,y)
print('loss:', loss.item())

# Backward pass
loss.backward()

##print out the gradients
print('dL/dw:',linear.weight.grad)
print('dL/db:',linear.bias.grad)

##1-step gradient descent*******************************
optimizer.step()

#print out the loss after 1-step gradient descent
pred = linear(x)
loss = criterion(pred,y)
print('loss after 1 step optimization:',loss.item())

## 3. loading data from numpy
x3 = np.array([[1,2],[3,4]])
y = torch.from_numpy(x3)
z=y.numpy()
print(z);print('\n')

## 4. input pipline

## download and construct CIFAR-10 dataset
train_dataset = torchvision.datasets.CIFAR10(root='../../data/',train=True,transform=transforms.ToTensor(),download=True)
## fetch one data pair(read data from disk)
image,label = train_dataset[0]
print(image.size())
print(label)

## input pipline for custom dataset

# class CustomDataset(torch.utils.data.Dataset):
#     def __init__(self):
#         # TODO
#         #1.Initialize file paths or a list of file names
#         pass
#     def __getitem__(self,index):
#         # TODO
#         # 1.Read one data from file (eg. using numpy.fromfile, PIL.Image.open).
#         # 2.Preprocess the data (eg. torchvision.Transform)
#         # 3.Return a data pair( e.g. image and label)
#         pass
#     def __len__(self):
#         return 0
#
#     custom_dataset = CustomDataset()
#     train_loader = torch.utils.data.DataLoader(dataset=custom_dataset,batch_size=64,shuffle=True)
#
#
#
#
