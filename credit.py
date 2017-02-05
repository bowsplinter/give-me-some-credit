import pandas as pd

from sklearn.ensemble import RandomForestRegressor

credit_df = pd.read_csv("cs-training.csv")
credit_test_df = pd.read_csv("cs-test.csv")

print credit_df.info()
print '--------------------'
print credit_test_df.info()

def replace98and96(column):
    new = []
    newval = column.max()
    for i in column:
        if (i == 96 | i == 98):
            new.append(newval)
        else:
            new.append(i)
    return new

def cleanHeaders(data):
    cleanCol = []
    for i in range(len(data.columns)):
        cleanCol.append(data.columns[i].replace('-', ''))
    data.columns = cleanCol

cleanHeaders(credit_df)
cleanHeaders(credit_test_df)

# Preprocessing

#fill in NaN values with median
credit_df["MonthlyIncome"].fillna(credit_df["MonthlyIncome"].median(), inplace=True)
credit_df["NumberOfDependents"].fillna(credit_df["NumberOfDependents"].median(), inplace=True)

credit_test_df = credit_test_df.drop("SeriousDlqin2yrs",axis=1)
credit_test_df["MonthlyIncome"].fillna(credit_test_df["MonthlyIncome"].median(), inplace=True)
credit_test_df["NumberOfDependents"].fillna(credit_test_df["NumberOfDependents"].median(), inplace=True)

# replace 96 and 98 with max
# credit_df.NumberOfTimes90DaysLate  = replace98and96(credit_df.NumberOfTimes90DaysLate)

# credit_df.NumberOfTime3059DaysPastDueNotWorse = replace98and96(credit_df.NumberOfTime3059DaysPastDueNotWorse)

# credit_df.NumberOfTime6089DaysPastDueNotWorse = replace98and96(credit_df.NumberOfTime6089DaysPastDueNotWorse)

credit_df = credit_df[credit_df.NumberOfTimes90DaysLate != 98]
credit_df = credit_df[credit_df.NumberOfTimes90DaysLate != 96]
# credit_df = credit_df[credit_df.NumberOfTime3059DaysPastDueNotWorse != 98]
# credit_df = credit_df[credit_df.NumberOfTime3059DaysPastDueNotWorse != 96]
# credit_df = credit_df[credit_df.NumberOfTime6089DaysPastDueNotWorse != 98]
# credit_df = credit_df[credit_df.NumberOfTime6089DaysPastDueNotWorse != 96]

# replace 96 and 98 with max
credit_test_df.NumberOfTimes90DaysLate  = replace98and96(credit_test_df.NumberOfTimes90DaysLate)
credit_test_df.NumberOfTime3059DaysPastDueNotWorse = replace98and96(credit_test_df.NumberOfTime3059DaysPastDueNotWorse)
credit_test_df.NumberOfTime6089DaysPastDueNotWorse = replace98and96(credit_test_df.NumberOfTime6089DaysPastDueNotWorse)

print credit_df.info()
print '---------------------'
print credit_test_df.info()

X_train = credit_df.drop("SeriousDlqin2yrs",axis=1)
Y_train = credit_df["SeriousDlqin2yrs"]
X_test  = credit_test_df

random_forest = RandomForestRegressor(n_estimators = 100)
random_forest.fit(X_train, Y_train)
Y_pred = random_forest.predict(X_test)
print random_forest.score(X_train, Y_train)

prediction = pd.DataFrame({
        "Id": credit_test_df["Id"],
        "Probability": Y_pred
    })
prediction.to_csv('submit.csv', index=False)
