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

# Takes random numbers and appends them to the empty lists made initially

for val in x_values: 
    x_values.append(r.randint(1, 100))

for val in y_values:
  y_values.append(r.randint(1, 100))

# Gets the values of the lists in order to begin graphing, gives the user an idea of what the values look like.

getListVals(x_values)

getListVals(y_values)

get_len(x_values)

makeBufferLine()

get_len(y_values)


if len(y_values) == len(x_values):
  plt.plot(x_values, y_values, marker = "*")
  plt.show()
else: 
  print("The two list lengths are not equal in length!")

  # "PLOT" KEYWORD CAN BE CHANGED TO ANY FORM TO GRAPH ANY DESIRED GRAPH
