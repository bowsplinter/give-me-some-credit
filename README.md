# Give Me Some Credit

My attempt at solving Kaggle's [Give Me Some Credit Problem](https://www.kaggle.com/c/GiveMeSomeCredit)

### Goal

Predict the probability that someone will experience financial distress in the next 2 years.

### Initial thoughts

A regression problem. Having worked with random forests before, decided to start with that as an attempt.

### Preprocessing

First examining the data, I noticed that both MonthlyIncome and NumberOfDependents had some missing data. The missing data was filled in with the median of each respective columns.

NumberOfTimes90DaysLate had some values that couldnt be true (98/96). Initially I had replaced these values with the median from the columns, but after more careful examination of the rows, I made the judgement call that the data should not be used for training the model. I reasoned that this would make my model better at predicting values with proper values while becoming worse at those with the error values. Looking at the sample data, with >99% of data having the proper values, this seemed reasonable.

### Kaggle
Private Score: 0.839176
Predicted private ranking: 693

### AUC
AUC is area under the ROC (Receiver Operating Characteristic) Curve. To use this to evaluate a regression curve, a decision rule is used to covert the probabilities into a postive/negative result. AUC uses the confusion matrix (True Postive/False Positive/True Negative/False Negative). Taking the True Positive rate and the False Positive Rate under different thresholds for logisitic regression, they are plotted on a graph. The closer a model comes to 1 for AUC, the better it is.

Another method of evaluating a model could be mean-squared error. The disadvantage of mean-squared error as compared to AUC is that mean-squared error penalizes single large errors, while tolerates multiple smaller errors. This could lead to a lower score for a model that has a large error for a few values but predicts the rest of the values accurately, compared to a model that consistently gives small errors for each value. Based on our needs, we might prefer the first model over the second.