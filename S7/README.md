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

[Assignment File](https://github.com/sagarigrandhi/EVA4/blob/master/S7/Assignment_7.ipynb)


### Architecture, Parameters and Hyperparameters:

Architecture: No Fully Connected Layer, Bias is not included.
```
INPUT -> [[CONV(k=3,s=1,p=1) -> BN -> RELU]*3 -> [CONV(k=1,s=1,p=0) -> BN -> RELU] -> POOL(2*2)] -> [[CONV(k=3,s=1,p=1) -> BN -> RELU] -> [CONV(k=3,s=1,p=2,d=2) -> BN -> RELU] -> [CONV(k=1,s=1,p=0) -> BN -> RELU] -> POOL(2*2)] -> [[CONV(k=3,s=1,p=1) -> BN -> RELU]*2 -> [CONV(k=1,s=1,p=0) -> BN -> RELU] -> POOL(2*2)] -> [[CONV(k=3,s=1,p=1,g=nin) -> BN -> RELU] -> [CONV(k=3,s=1,p=1) -> BN -> RELU]] -> GAP -> [CONV(k=1,s=1,p=0)]
```


Parameters: 439k

```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 64, 32, 32]           1,728
       BatchNorm2d-2           [-1, 64, 32, 32]             128
              ReLU-3           [-1, 64, 32, 32]               0
            Conv2d-4           [-1, 64, 32, 32]          36,864
       BatchNorm2d-5           [-1, 64, 32, 32]             128
              ReLU-6           [-1, 64, 32, 32]               0
            Conv2d-7          [-1, 128, 32, 32]          73,728
       BatchNorm2d-8          [-1, 128, 32, 32]             256
              ReLU-9          [-1, 128, 32, 32]               0
           Conv2d-10           [-1, 64, 32, 32]           8,192
      BatchNorm2d-11           [-1, 64, 32, 32]             128
             ReLU-12           [-1, 64, 32, 32]               0
        MaxPool2d-13           [-1, 64, 16, 16]               0
           Conv2d-14           [-1, 64, 16, 16]          36,864
      BatchNorm2d-15           [-1, 64, 16, 16]             128
             ReLU-16           [-1, 64, 16, 16]               0
           Conv2d-17          [-1, 128, 16, 16]          73,728
      BatchNorm2d-18          [-1, 128, 16, 16]             256
             ReLU-19          [-1, 128, 16, 16]               0
           Conv2d-20           [-1, 64, 16, 16]           8,192
      BatchNorm2d-21           [-1, 64, 16, 16]             128
             ReLU-22           [-1, 64, 16, 16]               0
        MaxPool2d-23             [-1, 64, 8, 8]               0
           Conv2d-24             [-1, 64, 8, 8]          36,864
      BatchNorm2d-25             [-1, 64, 8, 8]             128
             ReLU-26             [-1, 64, 8, 8]               0
           Conv2d-27            [-1, 128, 8, 8]          73,728
      BatchNorm2d-28            [-1, 128, 8, 8]             256
             ReLU-29            [-1, 128, 8, 8]               0
           Conv2d-30             [-1, 64, 8, 8]           8,192
      BatchNorm2d-31             [-1, 64, 8, 8]             128
             ReLU-32             [-1, 64, 8, 8]               0
        MaxPool2d-33             [-1, 64, 4, 4]               0
           Conv2d-34             [-1, 64, 4, 4]             576
           Conv2d-35             [-1, 64, 4, 4]           4,096
depthwise_separable_conv-36      [-1, 64, 4, 4]               0
      BatchNorm2d-37             [-1, 64, 4, 4]             128
             ReLU-38             [-1, 64, 4, 4]               0
           Conv2d-39            [-1, 128, 4, 4]          73,728
      BatchNorm2d-40            [-1, 128, 4, 4]             256
             ReLU-41            [-1, 128, 4, 4]               0
AdaptiveAvgPool2d-42            [-1, 128, 1, 1]               0
           Conv2d-43             [-1, 10, 1, 1]           1,280
================================================================
Total params: 439,808
Trainable params: 439,808
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.01
Forward/backward pass size (MB): 9.63
Params size (MB): 1.68
Estimated Total Size (MB): 11.32
----------------------------------------------------------------
```

Hyperparameters:
* Loss function - Cross-entropy loss
* Optimizer - SGD
* Batch size - 128
* Learning rate - 0.01
* Weight decay - 0.0003
* Dropout - None
* Receptive field - 98
* Epochs - 10
* Training Accuracy - 89.70%
* Validation Accuracy - 87.47%

### Receptive Field

Layer	| Nin |	k	| p | s |	Nout | Jout |	Rout
----- |-----|---|---|---|----- |----- |---
input|	0|	0|	0|	0|	32|	1|	1|
conv1|	32|	3|	1|	1|	32|	1|	3|
conv2|	32|	3|	1|	1|	32|	1|	5|
conv3|	32|	3|	1|	1|	32|	1|	7|
conv4|	32|	1|	0|	1|	32|	1|	7|
pool1|	32|	2|	0|	2|	16|	2|	8|
conv5|	16|	3|	1|	1|	16|	2|	12|
conv6|	16|	5|	2|	1|	16|	2|	20|
conv7|	16|	1|	0|	1|	16|	2|	20|
pool2|	16|	2|	0|	2|	8|	4|	22|
conv8|	8|	3|	1|	1|	8|	4|	30|
conv9|	8|	3|	1|	1|	8|	4|	38|
conv10|	8|	1|	0|	1|	8|	4|	38|
pool3|	8|	2|	0|	2|	4|	8|	42|
depthwise|	4|	3|	1|	1|	4|	8|	58|
pointwise|	4|	1|	0|	1|	4|	8|	58|
conv11|	4|	3|	1|	1|	4|	8|	74|
gap|	4|	4|	0|	1|	1|	8|	98|
conv12|	1|	1|	0|	1|	1|	8|	98|


### Train/Test Performance

Test Accuracy: 86 to 88%
```
Epoch : 10/10, Batch_id : 390, Training Loss : 0.2300,  Training Accuracy : 90.06%: 100%|██████████| 391/391 [00:46<00:00,  8.48it/s]

Test Loss : 0.379, Test Accuracy : 8688/10000 (86.88%)
```

### Loss and Accuracy
![Test Loss and Accuracy](https://github.com/sagarigrandhi/EVA4/blob/master/S7/Results/cifar10_test_loss_accuracy.png)

### Predictions
![Predictions](https://github.com/sagarigrandhi/EVA4/blob/master/S7/Results/cifar10_predicted_images.png)

### Misclassified Images
![Misclassified Images](https://github.com/sagarigrandhi/EVA4/blob/master/S7/Results/cifar10_misclassified_images.png)

### Class-Wise Accuracy
```
Accuracy of plane : 90 %
Accuracy of   car : 100 %
Accuracy of  bird : 85 %
Accuracy of   cat : 79 %
Accuracy of  deer : 82 %
Accuracy of   dog : 85 %
Accuracy of  frog : 96 %
Accuracy of horse : 89 %
Accuracy of  ship : 94 %
Accuracy of truck : 93 %
```

## Conclusion
* Achieved a test accuracy of ~87% in just 10 epochs and 80+ accuracy after 6th epoch with 439K parameters and a maximum RF of 98. By varying the number of epochs or number of parameters, accuracy can be improved.
* Random rotation and random horizontal flip were used to achieve the best test accuracy. By using additional data augmentation strategies, acccuracy can be improved.
