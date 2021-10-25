
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import random 
from PlantClassDatabase import PlantClass
from myFunctions import stop, makeBufferLine, getListVals, get_len
import csv 

df = pd.read_csv("venv/CSVFiles/MaxGrowthInPlantSpecies.csv")


Species = []


plant_species = df.iloc[:, 1]

plant_heights = df.iloc[:, 0]


label_vals = []

numerical_vals = []

for val in plant_species:
    label_vals.append(val)

for val in plant_heights:
    numerical_vals.append(val)

print(label_vals)

makeBufferLine()

print(numerical_vals)



plt.bar(label_vals, numerical_vals)
plt.show()






