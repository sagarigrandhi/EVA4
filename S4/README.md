# Session 4 Assignment

* 99.4% validation accuracy
* Less than 20k parameters
* Less than 20 epochs
* No fully connected layer

##  Architectural Basics 
* Layers to add in a network 
* Receptive Field
* 3x3 Convolutions
* MaxPooling - position, distance from prediction
* No of channels
* Image Normalization
* 1x1 Convolutions - position
* Transition layers - position
* Softmax
* Batch Normalization - position, distance from prediction
* Dropout - position, distance from the prediction
* Larger kernel or alternatives - When to stop convolutions and go ahead
* Performance - How do we know network is not doing well, comparatively, very early
* Batch Size - effects of batch size
* Learning Rate

[File](https://github.com/sagarigrandhi/EVA4/blob/master/S4/Assignment_4.ipynb)

* Validation Accuracy : 99.4%
```
Epoch: 19
Test set: Average loss: 0.0200, Accuracy: 9938/10000 (99.4%)

```
* Total Parameters: 12.5k

```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 8, 26, 26]              80
       BatchNorm2d-2            [-1, 8, 26, 26]              16
            Conv2d-3           [-1, 16, 24, 24]           1,168
       BatchNorm2d-4           [-1, 16, 24, 24]              32
            Conv2d-5           [-1, 32, 22, 22]           4,640
       BatchNorm2d-6           [-1, 32, 22, 22]              64
         MaxPool2d-7           [-1, 32, 11, 11]               0
            Conv2d-8            [-1, 8, 11, 11]             264
       BatchNorm2d-9            [-1, 8, 11, 11]              16
           Conv2d-10             [-1, 16, 9, 9]           1,168
      BatchNorm2d-11             [-1, 16, 9, 9]              32
           Conv2d-12             [-1, 32, 7, 7]           4,640
      BatchNorm2d-13             [-1, 32, 7, 7]              64
AdaptiveAvgPool2d-14             [-1, 32, 1, 1]               0
           Conv2d-15             [-1, 10, 1, 1]             330
================================================================
Total params: 12,514
Trainable params: 12,514
Non-trainable params: 0
----------------------------------------------------------------
```

* No of epochs: 19
* No Fully Connected Layer
