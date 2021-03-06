# -*- coding: utf-8 -*-
"""models.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HLEjLo8YjFF02JL440s2hZWCIQ_r0lkM
"""

# Imports
import torch.nn as nn
import torch.nn.functional as F

def conv_block(in_channels, out_channels, *args, **kwargs):
  '''
  Function to form a convolution block.

  :param in_channels: (int), number of channels in the input image
  :param out_channels: (int), number of channels after convolution
  
  :returns: (class), a sequential container of Convolution, BatchNorm and ReLU layers
  '''
  return nn.Sequential(
      nn.Conv2d(in_channels, out_channels, *args, **kwargs),
      nn.BatchNorm2d(out_channels),
      nn.ReLU()
      )
  
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()  
        # Input block
        self.conv1 = conv_block(in_channels=1, out_channels=10, kernel_size=3, padding=0, bias=False) # output = 26*26*10

        # Convolution block 1
        self.conv2 = conv_block(in_channels=10, out_channels=30, kernel_size=3, padding=0, bias=False) # output = 24*24*30
        
        # Transition block 1
        self.conv3 = conv_block(in_channels=30, out_channels=10, kernel_size=1, padding=0, bias=False) # output = 24*24*10
        self.pool = nn.MaxPool2d(2) # output = 12*12*10
        
        # Convolution block 2
        self.conv4 = conv_block(in_channels=10, out_channels=14, kernel_size=3, padding=0, bias=False) # output = 10*10*14
        # Convolution block 3
        self.conv5 = conv_block(in_channels=14, out_channels=14, kernel_size=3, padding=0, bias=False) # output = 8*8*14
        # Convolution block 4
        self.conv6 = conv_block(in_channels=14, out_channels=14, kernel_size=3,padding=0, bias=False) # output = 6*6*14
        # Convolution block 5
        self.conv7 = conv_block(in_channels=14, out_channels=14, kernel_size=3, padding=1, bias=False) # output = 6*6*14
        
        # GAP layer
        self.gap = nn.AdaptiveAvgPool2d(1) # output = 1*1*14
        # Output block
        self.conv8 = nn.Conv2d(in_channels = 14, out_channels=10, kernel_size=1, padding=0, bias=False) # output = 1*1*10
         
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.pool(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = self.conv6(x)
        x = self.conv7(x)
        x = self.gap(x)
        x = self.conv8(x)
        
        x = x.view(-1, 10)
        return F.log_softmax(x, dim=-1)