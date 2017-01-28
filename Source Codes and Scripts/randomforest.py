from sklearn.ensemble import RandomForestClassifier as RF
import numpy as np
import pandas as pd

input_file = "reformatedtraiin.csv"
data = pd.read_csv(input_file, header=0)
data = data.dropna()
X = data.ix[:,:-1]
y = data.ix[:,-1]

randomforest = RF(10)
randomforest.fit(X,y)

print(randomforest)

