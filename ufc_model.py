import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/conno/AppData/Local/Programs/projects/ufc_project/ufc-fighters-statistics.csv")

print(data.isnull().sum)