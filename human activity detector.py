import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn import metrics
from sklearn import preprocessing

def main():
    #reading data sets

    testf=pd.read_csv('test.csv')

    trainf=pd.read_csv('train.csv')

    #Preprocessing data

    le = preprocessing.LabelEncoder()

    le.fit(testf['Activity'])

    # print(le.transform(testf['Activity']))

    testf['Activity_Result']=le.transform(testf['Activity'])

    testf.drop(['Activity'], axis=1, inplace=True)

    ke = preprocessing.LabelEncoder()

    ke.fit(trainf['Activity'])

    trainf['Activity_Result'] = ke.transform(trainf['Activity'])

    trainf.drop(['Activity'],axis=1,inplace=True)

    # print(testf.head())

    # APPLYING  ML
    model=RandomForestClassifier(n_estimators = 30, random_state = 42)

    # print(testf.shape)

    Y_train =trainf['Activity_Result']
    X_train =trainf.drop(['Activity_Result'],axis=1)
    x_test =testf.drop(['Activity_Result'],axis=1)
    y_test= testf['Activity_Result']

    model.fit(X_train,Y_train)

    expected = y_test

    # Make Prediction
    predicted = model.predict(x_test)

    print(metrics.classification_report(expected, predicted))

    # Print Accuracy
    print(' Accuracy :'+str(metrics.accuracy_score(expected, predicted)))

    # Print number of correctly classified samples
    # print('number of correctly classified samples :'+str(metrics.accuracy_score(expected, predicted, normalize=False)))

main()