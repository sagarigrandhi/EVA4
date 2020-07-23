# Session 4 Assignment

## Objective

* 99.4% validation accuracy
* Less than 20k parameters
* Less than 20 epochs
* No fully connected layer

##  Architectural Basics 

* Image Normalization
* Batch Size - it's effects
* Receptive Field
* Network layers 
* Transition layers - position
* No of channels
* 3x3 Convolutions
* 1x1 Convolutions - position
* Batch Normalization - position, distance from prediction
* Dropout - position, distance from the prediction
* MaxPooling - position, distance from prediction
* Larger kernel or alternatives - When to stop convolutions and go ahead
* Softmax
* Learning Rate
* Performance - How do we know network is not doing well, comparatively, very early

## Results

[Assignment File](https://github.com/sagarigrandhi/EVA4/blob/master/S4/Assignment_4.ipynb)

Validation Accuracy : 99.4%

```
Epoch: 19
Test set: Average loss: 0.0200, Accuracy: 9938/10000 (99.4%)
```

Parameters: 12.5k

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

Epochs: 19

```
  0%|          | 0/1875 [00:00<?, ?it/s]
/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:28: UserWarning: Implicit dimension choice for log_softmax has been deprecated. Change the call to include dim=X as an argument.
loss=0.11956486105918884 batch_id=1874: 100%|██████████| 1875/1875 [00:21<00:00, 87.16it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0935, Accuracy: 9723/10000 (97.2%)

loss=0.009263277053833008 batch_id=1874: 100%|██████████| 1875/1875 [00:21<00:00, 89.17it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0469, Accuracy: 9858/10000 (98.6%)

loss=0.0057594627141952515 batch_id=1874: 100%|██████████| 1875/1875 [00:21<00:00, 87.83it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0370, Accuracy: 9889/10000 (98.9%)

loss=0.03366020321846008 batch_id=1874: 100%|██████████| 1875/1875 [00:20<00:00, 89.37it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0360, Accuracy: 9889/10000 (98.9%)

loss=0.002917453646659851 batch_id=1874: 100%|██████████| 1875/1875 [00:21<00:00, 89.20it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0273, Accuracy: 9907/10000 (99.1%)

loss=0.02572450041770935 batch_id=1874: 100%|██████████| 1875/1875 [00:20<00:00, 89.56it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0275, Accuracy: 9913/10000 (99.1%)

loss=0.00375249981880188 batch_id=1874: 100%|██████████| 1875/1875 [00:21<00:00, 88.65it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0272, Accuracy: 9913/10000 (99.1%)

loss=0.027218297123908997 batch_id=1874: 100%|██████████| 1875/1875 [00:20<00:00, 89.35it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0242, Accuracy: 9923/10000 (99.2%)

loss=0.001628786325454712 batch_id=1874: 100%|██████████| 1875/1875 [00:20<00:00, 89.73it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0252, Accuracy: 9917/10000 (99.2%)

loss=0.024715274572372437 batch_id=1874: 100%|██████████| 1875/1875 [00:21<00:00, 88.82it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0243, Accuracy: 9929/10000 (99.3%)

loss=0.06545257568359375 batch_id=1874: 100%|██████████| 1875/1875 [00:21<00:00, 88.87it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0240, Accuracy: 9927/10000 (99.3%)

loss=0.01260325312614441 batch_id=1874: 100%|██████████| 1875/1875 [00:21<00:00, 89.23it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0251, Accuracy: 9917/10000 (99.2%)

loss=0.00449785590171814 batch_id=1874: 100%|██████████| 1875/1875 [00:20<00:00, 90.36it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0255, Accuracy: 9924/10000 (99.2%)

loss=0.006565719842910767 batch_id=1874: 100%|██████████| 1875/1875 [00:20<00:00, 90.02it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0237, Accuracy: 9934/10000 (99.3%)

loss=0.002406895160675049 batch_id=1874: 100%|██████████| 1875/1875 [00:20<00:00, 89.94it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0203, Accuracy: 9937/10000 (99.4%)

loss=0.0003854036331176758 batch_id=1874: 100%|██████████| 1875/1875 [00:20<00:00, 89.38it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0215, Accuracy: 9935/10000 (99.3%)

loss=0.002652466297149658 batch_id=1874: 100%|██████████| 1875/1875 [00:21<00:00, 88.79it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0234, Accuracy: 9926/10000 (99.3%)

loss=0.0019318163394927979 batch_id=1874: 100%|██████████| 1875/1875 [00:20<00:00, 89.39it/s]
  0%|          | 0/1875 [00:00<?, ?it/s]
Test set: Average loss: 0.0214, Accuracy: 9934/10000 (99.3%)

loss=0.010960191488265991 batch_id=1874: 100%|██████████| 1875/1875 [00:20<00:00, 89.95it/s]

Test set: Average loss: 0.0200, Accuracy: 9938/10000 (99.4%)
```
Architecture: No Fully Connected Layer, Bias is included. 

```
INPUT -> [[CONV(k=3,s=1,p=0) -> BN -> RELU]*3 -> POOL(2*2)] -> [CONV(k=1,s=1,p=0) -> BN -> RELU] -> [[CONV(k=3,s=1,p=0) -> BN -> RELU]*2] -> GAP -> [CONV(k=1,s=1,p=0)] -> LOG_SOFTMAX 
```

## Conclusion

Only the last epoch shows 99.4% accuracy. Inorder to have consistency in the last 3 epochs, the position of pooling, number of channels in the architecture are some of the things that can be changed. 
