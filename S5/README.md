# Session 5 Assignment

* 99.4% validation accuracy (consistent in the last few epochs not a one-time achievement)
* Less than 10k parameters
* Less than or equal to 15 epochs
* Do it in minimum 5 steps
* Keep Receptive Field calculations handy for each of the models
* One file for each of the 5 steps and must have "target, result, analysis" block

## First Model

[File 1] (https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F1.ipynb)

### Target:
* Make the model lighter (14,14,20 and repeat)
* Add transition style architecture with GAP followed by 1*1 at the end to reduce the number of parameters.
 
### Results:
* Parameters: 9.1k
* Training Accuracy: 97.88
* Testing Accuracy: 97.88

### Analysis:
* No overfitting or underfitting (0 diff).
* Good model!. Model can be pushed to get better accuracy.

## Second Model

[File 2] (https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F2.ipynb)

### Target:
* Add BatchNorm to increase model efficiency.
 
### Results:
* Parameters: 9.3k
* Training Accuracy: 99.38
* Testing Accuracy: 99.04

Best Testing Accuracy: 99.16 (13th epoch)

### Analysis:
* Model started overfitting now (0.38 diff). 
* Better accuracy but may need to add more capacity, especially at the end. Since we know that mnist can be stopped at an RF of 5*5.

## Third Model

[File 3] (https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F3.ipynb)

### Target:
* Increase model capacity by adding another layer at the end since mnist can be stopped at 5*5 RF. 
* Changed pattern to 10,10,16,30 pattern to get < 10k parameters.
 
### Results:
* Parameters: 9.7k 
* Training Accuracy: 99.43
* Testing Accuracy: 99.16

Best Testing Accuracy: 99.18 (7th epoch)

### Analysis:
* Overfitting reduced slightly (0.27 diff). 
* Accuracy improved slightly, we may want to change the position of maxpooling as a closer analysis of MNIST reveals that just at RF of 5x5 we start to see patterns forming. 

## Fourth Model

[File 4] (https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F4.ipynb)

### Target: 
* Peform maxpooling at 5*5 RF.
* Changed pattern to 10,30,10,14,14,14 pattern to get < 10k parameters.
 
### Results:
* Parameters: 9.9k
* Training Accuracy: 99.46
* Testing Accuracy: 99.34

Best Testing Accuracy: 99.37 (13th epoch)

### Analysis:
* Overfitting reduced even more (0.12 diff).We can add a slight rotation to reduce the overfitting.
* Much better accuracy but we don't see 99.4.

## Fifth Model

[File 5] (https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F5.ipynb)

### Target:
* Add rotation, a small amount should be sufficient (10 degrees).
 
### Results:
* Parameters: 9.9k
* Training Accuracy: 99.20
* Testing Accuracy: 99.51

Consistent for 12,13,14 epochs - 99.47, 99.48, 99.51.

### Analysis:
* Model started underfitting now (0.31 diff). It is fine since we have made it harder to train.
* Model crossed 99.4. It means that the test images has a few images that had a transformation difference wrt the train images. 
* Try using LR scheduler to go beyond 99.5.

## Sixth Model - Additional

[File 6] (https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F6.ipynb)

### Target:
* Add LR Scheduler with a step LR, gamma of 0.1 after every 6 steps.
 
### Results:
* Parameters: 9.9k
* Training Accuracy: 99.24
* Testing Accuracy: 99.52

Best Testing Accuracy - 99.55 (12th epoch)

Consistent for 12,13,14 epochs - 99.55, 99.53, 99.52

### Analysis:
* Underfitting reduced slightly (0.28 diff).
* Model crossed 99.5 faster but final accuracy is not more than 99.55.
* Try using OneCycleLR to reach 99.6.

## Seventh Model - Additional

[File 7] (https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F7.ipynb)

### Target:
* Add LR Scheduler - OneCycleLR (total_steps - 15, max_lr - 0.1)
* Change batch size to 32 to improve the test accuracy.
 
### Results:
* Parameters: 9.9k
* Training Accuracy: 99.44
* Testing Accuracy: 99.60

Best Testing Accuracy: 99.61 (12th epoch)

Consistent for 12,13,14 epochs - 99.61, 99.60, 99.60

### Analysis:
* Underfitting reduced even more (0.16 diff).
* OneCycleLR worked best. Final accuracy is 99.6.
* Aim for < 8k parameters.