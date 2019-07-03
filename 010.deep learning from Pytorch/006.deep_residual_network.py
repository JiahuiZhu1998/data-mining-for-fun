'''
Name: Jiahui Zhu
Date: 7/2/2019
'''

import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transform

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

num_epochs = 80
learning_rate = 0.001

transform = transform.Compose([
    transform.Pad(4),
    transform.RandomHorizontalFlip(),
    transform.RandomCrop(32),
    transform.ToTensor()
])

train_dataset=torchvision.datasets.CIFAR10(root='../../data/',train=True, transform=transform,download=True)
test_dataset=torchvision.datasets.CIFAR10(root='../../data/',train=False,transform=transform.ToTensor())
train_loader=torchvision.utils.data.loader(dataset=train_dataset,batch_size=100,shuffle=True)
test_loader=torchvision.utils.data.loader(dataset=test_dataset,batch_size=100,shuffle=False)

def conv3x3(in_channel,out_channel,stride=1):
    return nn.Conv2d(in_channel,out_channel,kernel_size=3,stride=stride,padding=1,bias=False)

class ResidualBlock():
    pass