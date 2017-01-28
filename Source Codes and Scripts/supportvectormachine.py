"""
This script creates a support vector machine and trains it
on data formatted in the format that train.csv uses.
It uses the scikit learn library's implementation.
"""

from sklearn.svm import SVC
import numpy as np
import pandas as pd

#open and read file
input_file = "train_2014_q4_b.csv" #change this to train.csv if you like 
data = pd.read_csv(input_file, header=0)
data = data.dropna()
X = data.ix[:,:-1]
y = data.ix[:,-1]
#X can be further sliced here
SVM = SVC()
SVM.fit(X,y)

print(SVM)
#make sure you slice the test_file to match the params in X
test_file = "test_b.csv"
test_data = pd.read_csv(test_file, header=0)

predictions = SVM.predict(test_data)

output_file = open("svm_predictions.csv", 'w')
np.savetxt(output_file, predictions)
