# -*- coding: utf-8 -*-
"""models.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16N9Lntk7CDncM7yS-UfSV-Vg9rVsRjQ8
"""

import torch.nn as nn
import torch.nn.functional as F

def conv_block(in_channels, out_channels, *args, **kwargs):
  '''
  Function to form a convolution block.

  :param in_channels: (int), number of channels in the input 
  :param out_channels: (int), number of channels after convolution
  
  :returns: (class), a sequential container of Convolution, BatchNorm and ReLU layers
  '''
  return nn.Sequential(
      nn.Conv2d(in_channels, out_channels, *args, **kwargs),
      nn.BatchNorm2d(out_channels),
      nn.ReLU()
      )

class depthwise_separable_conv(nn.Module):
  ''' Depthwise Convolution + Pointwise Convolution'''
  def __init__(self, nin , nout, stride = 1):
    super(depthwise_separable_conv, self).__init__()
    self.depthwise = nn.Conv2d(nin, 
                               nin, 
                               kernel_size = 3, 
                               stride = stride, 
                               padding = 1, 
                               groups = nin, 
                               bias =  False) 
    self.pointwise = nn.Conv2d(nin, 
                               nout, 
                               kernel_size = 1, 
                               stride = 1, 
                               padding = 0, 
                               bias = False) 

  def forward(self, x):
    x = self.depthwise(x) 
    x = self.pointwise(x)
    return x


class CIFAR10_Net(nn.Module):
    def __init__(self):
        super(CIFAR10_Net, self).__init__()
        # Convolution block 1
        self.conv1 = conv_block(in_channels=3, 
                                out_channels=64, 
                                kernel_size=3, 
                                padding=1, 
                                bias=False) # output = 32*32*64, RF = 3*3 
        
        # Convolution block 2
        self.conv2 = conv_block(in_channels=64, 
                                out_channels=64, 
                                kernel_size=3, 
                                padding=1,
                                bias=False) # output = 32*32*64, RF = 5*5  
        
        # Convolution block 3
        self.conv3 = conv_block(in_channels=64,
                                out_channels=128, 
                                kernel_size=3, 
                                padding=1, 
                                bias=False) # output = 32*32*128, RF = 7*7

        # Transition block 1 
        self.conv4 = conv_block(in_channels=128, 
                                out_channels=64, 
                                kernel_size=(1, 1), 
                                padding=0, 
                                bias=False) # output = 32*32*64, RF = 7*7
        self.pool1 = nn.MaxPool2d(2) # output = 16*16*64, RF = 8*8

        # Convolution block 4
        self.conv5 = conv_block(in_channels=64, 
                                out_channels=64, 
                                kernel_size=3, 
                                padding=1,
                                bias=False) # output = 16*16*64, RF = 12*12 
        
        # Convolution block 5
        self.conv6 = conv_block(in_channels=64, 
                                out_channels=128, 
                                kernel_size=3,
                                padding=2,
                                dilation=2,
                                bias=False) # output = 16*16*128, RF = 20*20
         
        # Transition block 2
        self.conv7 = conv_block(in_channels=128, 
                                out_channels=64, 
                                kernel_size=(1, 1), 
                                padding=0, 
                                bias=False) # output = 16*16*64, RF = 20*20
        self.pool2 = nn.MaxPool2d(2) # output = 8*8*64, RF = 22*22
        
        # Convolution block 6
        self.conv8 = conv_block(in_channels=64, 
                                out_channels=64, 
                                kernel_size=3, 
                                padding=1,
                                bias=False) # output = 8*8*64, RF = 30*30
        
        # Convolution block 7
        self.conv9 = conv_block(in_channels=64, 
                                out_channels=128, 
                                kernel_size=3,
                                padding=1,
                                bias=False) # output = 8*8*128, RF = 38*38 

        # Transition block 3
        self.conv10 = conv_block(in_channels=128, 
                                 out_channels=64, 
                                 kernel_size=(1, 1),
                                 padding=0, 
                                 bias=False) # output = 8*8*64, RF = 38*38
        self.pool3 = nn.MaxPool2d(2) # output = 4*4*64, RF = 42*42
        
        # Depthwise separable convolution
        self.depthwise = nn.Sequential(
            depthwise_separable_conv(64, 64), 
            nn.BatchNorm2d(64),
            nn.ReLU()
        ) # output = 4*4*64, RF = 58*58
        
        # Convolution block 8
        self.conv11 = conv_block(in_channels=64,
                                 out_channels=128, 
                                 kernel_size=3, 
                                 padding=1,
                                 bias=False) # output = 4*4*128, RF = 74*74 
       
        ## Output block
        # GAP layer
        self.gap = nn.AdaptiveAvgPool2d(1) # output = 1*1*128, RF = 98*98
        # Fully-connected layer
        self.conv12 = nn.Conv2d(in_channels = 128, 
                                 out_channels = 10, 
                                 kernel_size = (1, 1), 
                                 padding = 0, 
                                 bias = False) # output = 1*1*10, RF = 98*98

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(self.pool1(x))
        x = self.conv6(x)
        x = self.conv7(x)
        x = self.conv8(self.pool2(x))
        x = self.conv9(x)
        x = self.conv10(x)
        x = self.depthwise(self.pool3(x))
        x = self.conv11(x)
        x = self.gap(x)
        x = self.conv12(x)
        x = x.view(-1, 10)
        return x