import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import random
from myFunctions import get_len, makeBufferLine, getListVals

r = random

x_values = []

y_values = []


for i in range(72):
  x_values.append(0)
  y_values.append(0)


for val in x_values: 
    x_values.append(r.randint(1, 100))

for val in y_values:
  y_values.append(r.randint(1, 100))

  
getListVals(x_values)

getListVals(y_values)

get_len(x_values)


makeBufferLine()

get_len(y_values)


#if len(y_values) == len(x_values):
 # plt.plot(x_values, y_values, marker = "*")
 # plt.show()
#else: 
  #print("The two list lengths are not equal in length!")

