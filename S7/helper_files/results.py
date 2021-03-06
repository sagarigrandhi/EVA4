# -*- coding: utf-8 -*-
"""results.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/190-1wpuUj8aniq2SZ3JvLzEqA36OAUGU
"""

import torch
import matplotlib.pyplot as plt
import numpy as np
from data_utils import deprocess

def visualize_graph(filepath, train_loss, test_loss, train_accuracy, test_accuracy):
  '''
  Function to visualize the training and test loss and accuracy graphs.

  :param filepath: (string), path to store the figure.
  :param train_loss: (list), list of losses during training
  :param test_loss: (list), list of losses during testing
  :param train_accuracy: (list), list of accuracies during training
  :param test_accuracy: (list), list of accuracies during testing
  '''
  fig, axs = plt.subplots(2, 2, figsize = (12, 8))
  # Plot training loss
  axs[0, 0].plot(train_loss)
  axs[0, 0].set_title('Training Loss Curve')
  axs[0, 0].set_xlabel('Epochs')
  axs[0, 0].set_ylabel('Training Loss')
  # Plot training accuracy
  axs[0, 1].plot(train_accuracy)
  axs[0, 1].set_title('Training Accuracy Curve')
  axs[0, 1].set_xlabel('Epochs')
  axs[0, 1].set_ylabel('Training Accuracy')
  # Plot test loss
  axs[1, 0].plot(test_loss)
  axs[1, 0].set_title('Test Loss Curve')
  axs[1, 0].set_xlabel('Epochs')
  axs[1, 0].set_ylabel('Test Loss')
  # Plot test accuracy
  axs[1, 1].plot(test_accuracy)
  axs[1, 1].set_title('Test Accuracy Curve')
  axs[1, 1].set_xlabel('Epochs')
  axs[1, 1].set_ylabel('Test Accuracy')
  fig.tight_layout()
  fig.savefig(filepath + '/EVA_figures/cifar10_train_test_loss_accuracy.png')
  
def visualize_predictions(filepath, device, model, test_loader, classes):
  '''
  Function to visualize the predictions of the test set.

  :param filepath: (string), path to store the figure
  :param device: (class), either CUDA or CPU
  :param model: (class), defined CNN model
  :param test_loader: (class), dataloader for the test data
  :param classes: (tuple), tuple of class names for the images
  '''
  # Get random test samples
  images, labels = next(iter(test_loader))
  images, labels = images.to(device), labels.to(device)
  output = model(images)
  _, pred = torch.max(output, 1)
  
  # Plot the images along with their labels and predictions
  fig = plt.figure(figsize = (8, 4))
  
  # Display the images
  for idx in range(10):
    ax = fig.add_subplot(2, 5, idx+1, xticks=[], yticks=[])
    ax.imshow(deprocess(images[idx]))
    plt.tight_layout()
    fig.suptitle('Predicted Images (Predicted (Actual))', fontsize = 10)
    ax.set_title('{} ({})'.format(classes[pred[idx]], classes[labels[idx]]), 
               color=('green' if pred[idx] == labels[idx].item() else 'red'),fontsize=9)
    fig.savefig(filepath + '/EVA_figures/cifar10_predicted_images.png');
    
def visualize_misclassified(filepath, misclassified, misclassified_num=25):
  '''
  Function to visualize the misclassified images for the model.

  :param misclassified: (list), list of misclassified images
  :param misclassified_num: (int), threshold for the number of misclassified images
  '''

  # Display the misclassified images
  fig = plt.figure(figsize = (12, 8))
  for i in range(misclassified_num):
    ax = fig.add_subplot(5, 5, i+1, xticks=[], yticks=[])
    ax.imshow(deprocess(misclassified[i][0]))
    fig.suptitle(' Misclassified Images (Predicted (Actual))', fontsize = 12, y=0.94)
    ax.set_title("{} ({})".format(misclassified[i][1], misclassified[i][2]), color="red", fontsize=9)
    fig.savefig(filepath + '/EVA_figures/cifar10_misclassified_images.png');
    

def classwise_accuracy(device, model, classes, test_loader):
  '''
  Function to display class-wise accuracies of the model.

  :param device: (class), either CUDA or CPU
  :param model: (class), defined CNN model
  :param classes: (tuple), tuple of class names for the images
  :param test_loader: (class), dataloader for the test data
  '''
  class_correct = list(0. for i in range(10))
  class_total = list(0. for i in range(10))

  with torch.no_grad():
    for batch_idx , (data, target) in enumerate(test_loader):
      # Get the samples
      images, labels = data.to(device), target.to(device)
     
      # Forward pass
      output = model(images)

      # Predict
      _, predict = torch.max(output, 1)
      c = (predict == labels).squeeze()

      # Calculate accuracies per class
      for i in range(4):
        label = labels[i]
        class_correct[label] += c[i].item()
        class_total[label] += 1
  for i in range(10):
    print('Accuracy of %5s : %2d %%' % (classes[i], 100 * class_correct[i] / class_total[i]))