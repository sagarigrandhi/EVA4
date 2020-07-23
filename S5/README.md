# Session 5 Assignment

## Objective

* 99.4% validation accuracy (consistent in the last few epochs not a one-time achievement)
* Less than 10k parameters
* Less than or equal to 15 epochs
* Do it in minimum 5 steps
* Keep Receptive Field calculations handy for each of the models
* One file for each of the 5 steps and must have "target, result, analysis" block

## Results

### First Model
[Assignment File 1](https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F1.ipynb)

#### Target
* Make the model lighter (14,14,20 and repeat)
* Add transition style architecture with GAP followed by 1*1 at the end to reduce the number of parameters.
 
#### Results
* Parameters: 9.1k
* Training Accuracy: 97.88%
* Test Accuracy: 97.88%

#### Analysis
* No overfitting or underfitting (0 diff).
* Good model!. Model can be pushed to get better accuracy.

### Second Model
[Assignment File 2](https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F2.ipynb)

#### Target
* Add BatchNorm to increase model efficiency.
 
#### Results
* Parameters: 9.3k
* Training Accuracy: 99.38%
* Test Accuracy: 99.04%

Best Test Accuracy: 99.16% (13th epoch)

#### Analysis
* Model started overfitting now (0.38 diff). 
* Better accuracy but may need to add more capacity, especially at the end. Since we know that mnist can be stopped at an RF of 5*5.

### Third Model
[Assignment File 3](https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F3.ipynb)

#### Target
* Increase model capacity by adding another layer at the end since mnist can be stopped at 5*5 RF. 
* Changed pattern to 10,10,16,30 pattern to get < 10k parameters.
 
#### Results
* Parameters: 9.7k 
* Training Accuracy: 99.43%
* Test Accuracy: 99.16%

Best Test Accuracy: 99.18% (7th epoch)

#### Analysis
* Overfitting reduced slightly (0.27 diff). 
* Accuracy improved slightly, we may want to change the position of maxpooling as a closer analysis of MNIST reveals that just at RF of 5x5 we start to see patterns forming. 

### Fourth Model
[Assignment File 4](https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F4.ipynb)

#### Target
* Peform maxpooling at 5*5 RF.
* Changed pattern to 10,30,10,14,14,14 pattern to get < 10k parameters.
 
#### Results
* Parameters: 9.9k
* Training Accuracy: 99.46%
* Test Accuracy: 99.34%

Best Test Accuracy: 99.37% (13th epoch)

#### Analysis
* Overfitting reduced even more (0.12 diff).We can add a slight rotation to reduce the overfitting.
* Much better accuracy but we don't see 99.45.

### Fifth Model
[Assignment File 5](https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F5.ipynb)

#### Target
* Add rotation, a small amount should be sufficient (10 degrees).
 
#### Results
* Parameters: 9.9k
* Training Accuracy: 99.20%
* Test Accuracy: 99.51%

Consistent for 12,13,14 epochs - 99.47%, 99.48%, 99.51%.

#### Analysis
* Model started underfitting now (0.31 diff). It is fine since we have made it harder to train.
* Model crossed 99.4%. It means that the test images has a few images that had a transformation difference wrt the train images. 
* Try using LR scheduler to go beyond 99.5%.

### Sixth Model - Additional
[Assignment File 6](https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F6.ipynb)

#### Target
* Add LR Scheduler with a step LR, gamma of 0.1 after every 6 steps.
 
#### Results
* Parameters: 9.9k
* Training Accuracy: 99.24%
* Test Accuracy: 99.52%

Best Test Accuracy - 99.55% (12th epoch)

Consistent for 12,13,14 epochs - 99.55%, 99.53%, 99.52%

#### Analysis
* Underfitting reduced slightly (0.28 diff).
* Model crossed 99.5% faster but final accuracy is not more than 99.55%.
* Try using OneCycleLR to reach 99.6%.

### Seventh Model - Additional
[Assignment File 7](https://github.com/sagarigrandhi/EVA4/blob/master/S5/Assignment_5_F7.ipynb)

#### Target
* Add LR Scheduler - OneCycleLR (total_steps - 15, max_lr - 0.1)
* Change batch size to 32 to improve the test accuracy.
 
#### Results
* Parameters: 9.9k
* Training Accuracy: 99.44%
* Test Accuracy: 99.60%

Best Test Accuracy: 99.61% (12th epoch)

Consistent for 12,13,14 epochs - 99.61%, 99.60%, 99.60%

#### Analysis:
* Underfitting reduced even more (0.16 diff).
* OneCycleLR worked best. Final accuracy is 99.6%.
* Aim for <8k parameters.

## Receptive Field 

Layer	| Nin |	k	| p | s |	Nout | Jout |	Rout
----- |-----|---|---|---|----- |----- |---
input|	0|	0|	0|	0|	28|	1|	1|
convblock1|	28|	3|	0|	1|	26|	1|	3|
convblock2|	26|	3|	0|	1|	24|	1|	5|
convblock3|	24|	1|	0|	1|	24|	1|	5|
pool1|	24|	2|	0|	2|	12|	2|	6|
convblock4|	12|	3|	0|	1|	10|	2|	10|
convblock5|	10|	3|	0|	1|	8|	2|	14|
convblock6|	8|	3|	0|	1|	6|	2|	18|
convblock7|	6|	3|	1|	1|	6|	2|	22|
gap|	6|	6|	0|	1|	1|	2|	32|
convblock8|	1|	1|	0|	1|	1|	2|	32|

## Conclusion

The number of parameters now are 9.9k. Further we can aim to reduce the parameters to less than 8k and try to achieve the objective.
