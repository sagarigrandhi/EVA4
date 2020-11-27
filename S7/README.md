# Session 7 Assignment

## Objective
Fix the code such that:
* The code uses GPU.
* The architecture is C1-C2-C3-C4-O (basically 3 MPs)
* Total RF must be more than 44.
* One of the layers must use Depthwise Separable Convolution.
* One of the layers must use Dilated Convolution.
* Use GAP (mandatory), add FC after GAP to target the number of classes.
* Achieve 80% accuracy with as many epochs as needed.
* Total parameters must be less than 1M.

## Results
Assignment File

### Parameters and Hyperparameters - 
* Loss function - Cross-entropy loss
* Optimizer - SGD
* Batch size - 128
* Learning rate - 0.01
* Weight decay - 0.0003
* Dropout - None
* Parameters - 439k
* Receptive field - 98
* Epochs - 10
* Training Accuracy - 89.70%
* Validation Accuracy - 87.47%

### Parameters 

### Train/Test Performance

### Receptive Field

### Loss and Accuracy

### Predictions

### Misclassified Images

### Class-wise Accuracy

## Conclusion
