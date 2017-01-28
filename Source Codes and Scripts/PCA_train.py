import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import math

data = pd.read_csv(filepath_or_buffer = "smalltrain.csv", header=None, sep=",")


choo_choo = open("train.csv")
labels = choo_choo.readline().strip().split(",")
data.columns=labels
data.dropna(how="all", inplace=True)
print(data.tail()) #display last 5 rows
label_dict = { k:v for k,v in enumerate(labels[:-1]) }
feature_dict = { k:v for k,v in enumerate(labels[-1:]) }

X = data.ix[:,0:len(label_dict)].values
y = data.ix[:,len(label_dict)].values

with plt.style.context('seaborn-whitegrid'):
    plt.figure(figsize=(8,6))
    for cnt in range(len(feature_dict)):
        plt.subplot(2,2, cnt+1)
        for lab in label_dict.values():
            plt.hist(X[y==lab, cnt], label=lab, bins=10, alpha=.3)
        plt.xlabel(feature_dict[cnt])
    plt.legend(loc='upper right', fancybox=True, fontsize=8)
    
    plt.tight_layout()
    plt.show()



