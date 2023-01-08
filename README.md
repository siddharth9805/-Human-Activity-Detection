# Human-Activity-Detection

#### About the Project

The Human Activity Recognition database was built from the recordings of 30 study participants performing activities of daily living (ADL) while carrying a waist-mounted smartphone with embedded inertial sensors. The objective is to classify activities into one of the six activities performed.



#### Descriptionof experiment

The experiments have been carried out with a group of 30 volunteers within an age bracket of 19-48 years. Each person performed six activities (WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING) wearing a smartphone (Samsung Galaxy S II) on the waist. Using its embedded accelerometer and gyroscope, we captured 3-axial linear acceleration and 3-axial angular velocity at a constant rate of 50Hz. The experiments have been video-recorded to label the data manually. The obtained dataset has been randomly partitioned into two sets, where 70% of the volunteers was selected for generating the training data and 30% the test data. 
The sensor signals (accelerometer and gyroscope) were pre-processed by applying noise filters and then sampled in fixed-width sliding windows of 2.56 sec and 50% overlap (128 readings/window). The sensor acceleration signal, which has gravitational and body motion components, was separated using a Butterworth low-pass filter into body acceleration and gravity. The gravitational force is assumed to have only low frequency components, therefore a filter with 0.3 Hz cutoff frequency was used. From each window, a vector of features was obtained by calculating variables from the time and frequency domain.

#### Approach For Solving The Problem 

1.	Read the train and test dataset using pandas library 
2.	Converted the target column for into number using label encoding which is present in scikit learn 
3.	Drop the column which doesn't affect the accuracy
4.	Applied RandomForestClassifier for this problem using scikit learn library 
5.	Divided the train dataset into x_train and y_train for training the model
6.	Divided the test dataset into y_train and y_test for finding the accuracy score of the model

####Conclusion

Accuracy Score is 0.9256871394638616
Precision score is 0.93   and recall score is 0.93
