import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Specialty Surgeries to Date.csv")
print(data)
print(data.columns)
sns.relplot(x="entity",y="value",data=data)
