# Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn










# ***********************************   EXPLORATORY ANALYSIS  ***********************************

# Reading Data Frame 
pd.set_option('display.max_columns', None)
df = pd.read_csv("train.csv", index_col='id')
df.head(10)
df.shape