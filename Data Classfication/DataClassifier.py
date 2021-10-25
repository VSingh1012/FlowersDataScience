import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


#If needed, code can be copied for classifier, since I have not been able to finish it, I am leaving it to the interested github user. 

df = pd.read_csv("venv/CSVFiles/iris.csv")


def get_column_names():
    print(df.columns)



def show_details():
    print(df.shape)
    print(df.size)
    

def getEncoding(): 
    X = df.iloc[:, 1:4]
    Y = df.iloc[:, 4]

    LabelEncoder_Y = LabelEncoder()
    Y = LabelEncoder_Y.fit_transform(Y)

    print(Y)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)
    

    


getEncoding()