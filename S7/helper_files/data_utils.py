# -*- coding: utf-8 -*-
"""data_utils.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vv0jwScELysnVszk7G9svT7hE6MaNy6r
"""

import torch
import matplotlib.pyplot as plt
import numpy as np
from torch.utils.data import DataLoader

def deprocess(image):
  # Remove all dimensions of size 1 from the tensor
  image = image.cpu().squeeze()
  # Remove the normalization
  image = image / 2 + 0.5 
  # Change the dimensions from CxHxW to HxWxC
  image = image.permute(1,2,0)
  # Clamp to get rid of numerical errors
  image = image.clamp(0, 1)
  return image
  
def data_statistics(training, train_loader, testing, test_loader):
  trainloader = DataLoader(training, shuffle = True, batch_size = len(training), num_workers = 2)
  train_iter = iter(trainloader)
  images, labels = train_iter.next()
  print('\nTraining data statistics:')
  print(' - Numpy Shape:', images.numpy().shape)
  print(' - Tensor Shape:', images.size())
  print(' - min:', torch.min(images).item())
  print(' - max:', torch.max(images).item())
  print(' - mean:', torch.mean(images).item()) 
  print(' - std:', torch.std(images).item()) 
  print(' - var:', torch.var(images).item())
  
  trainiter = iter(train_loader)
  train_images, train_labels = trainiter.next()
  print(' - Images Shape:', train_images.size())
  print(' - Labels:', train_labels.size())

  testloader = DataLoader(testing, shuffle = True, batch_size = len(testing), num_workers = 2)
  test_iter = iter(testloader)
  images, labels = test_iter.next()
  print('\nTest data statistics:')
  print(' - Numpy Shape:', images.numpy().shape)
  print(' - Tensor Shape:', images.size())
  print(' - min:', torch.min(images).item())
  print(' - max:', torch.max(images).item())
  print(' - mean:', torch.mean(images).item()) 
  print(' - std:', torch.std(images).item())
  print(' - var:', torch.var(images).item())
  
  testiter = iter(test_loader)
  test_images, test_labels = testiter.next()
  print(' - Images Shape:', test_images.size())
  print(' - Labels:', test_labels.size())

def visualize_data(train_loader, test_loader, classes):
  '''
  Function to visualize the training and test dataset.
  
  :param train_loader: (class), dataloader for the training data
  :param test_loader: (class), dataloader for the test data
  :param classes: (tuple), tuple of class names for the images
  '''
  # Obtain a batch of training images
  images, labels = next(iter(train_loader))
  # Plot the images along with their labels
  fig = plt.figure(figsize = (8,4))
  # Display the images
  for idx in range(10):
    ax = fig.add_subplot(2, 5, idx+1, xticks=[], yticks=[])
    ax.imshow(deprocess(images[idx]))
    plt.tight_layout()
    fig.suptitle('Training Images', fontsize = 10)
    ax.set_title('{}'.format(classes[labels[idx]]), fontsize=9)

  # Obtain a batch of test images
  images, labels = next(iter(test_loader))
  # Plot the images along with their labels
  fig = plt.figure(figsize = (8,4))
  # Display the images
  for idx in range(10):
    ax = fig.add_subplot(2, 5, idx+1, xticks=[], yticks=[])
    ax.imshow(deprocess(images[idx]))
    plt.tight_layout()
    fig.suptitle('Test Images', fontsize = 10)
    ax.set_title('{}'.format(classes[labels[idx]]), fontsize=9)