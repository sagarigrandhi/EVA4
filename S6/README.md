# Session 6 Assignment

## Objective
* Take the 5th code from session 5 assignment and run the model for 40 epochs with ~9K parameters: 
  1. Without L1/L2 Regularization
  2. With L1 Regularization
  3. With L2 Regularization
  4. With L1 and L2 Regularization
* Draw 2 graphs to show the test accuracy and loss change with legends, titles etc.
* Find any 25 misclassified images for L1 and L2 models with the actual and predicted class names.

## Results
### Analysis of the regularization parameters for L1 and L2 Regularization
1. The regularization parameter (lamda1) for L1 was chosen to be 1e-6 as this value had the least test loss and also the loss curve was smooth.

2. The regularization parameter (lamda2) for L2 was chosen to be 3e-5 as this value had the least test loss and also the loss curve was smooth.

### Train and Test Accuracy of the Models
| Models | Train Accuracy (%) | Test Accuracy (%) |
| --- | --- | --- |
| Without L1/L2 Regularization | 99.45 | 99.34 |
| With L1 Regularization (lamda1 = 1e-6) | 99.56 | 99.43 |
| With L2 Regularization (lamda2 = 3e-5) | 99.62 | 99.44 |
| With L1 and L2 Regularization (lambda1 = 1e-6, lamda2 = 3e-5) | 99.57 | 99.43 |

### Effect of L1 and L2 Regularization on Test Loss and Accuracy
![Validation Loss and Accuracy](https://github.com/sagarigrandhi/EVA4/blob/master/S6/Results/train_test_loss_accuracy.png)

### 25 Misclassified Images of the Models
![L1 Misclassified Images](https://github.com/sagarigrandhi/EVA4/blob/master/S6/Results/L1_misclassified_images.png)
![L2 Misclassified Images](https://github.com/sagarigrandhi/EVA4/blob/master/S6/Results/L2_misclassified_images.png)

## Conclusion
1. While the values for the regularization parameters of L1 and L2 regularization were chosen manually by repeatedly testing whether each of the values reduced the test loss, a better approach of tuning these hyperparameters can be done by using grid search.

2. Visualizing the misclassified images give us information of the kind of images that the model fails on. Based on this information, additional measures can be taken while training such as adding different data augmentation strategies to include similar images in the training set. 
