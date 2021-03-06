# -*- coding: utf-8 -*-
"""cuda_setup.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dr4ILBO1bhayjUVD0dDqTCdu7fcdBe19
"""

# Imports
import torch

def set_device():
  # Define the device to be CUDA if CUDA is available
  use_cuda = torch.cuda.is_available()
  device = torch.device("cuda" if use_cuda else "cpu")
  return device