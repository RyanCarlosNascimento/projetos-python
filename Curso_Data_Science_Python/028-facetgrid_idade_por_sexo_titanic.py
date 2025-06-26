import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data_frame = pd.read_csv('Titanic-Dataset.csv')

data_frame = pd.read_csv('Titanic-Dataset.csv')
g = sns.FacetGrid(data = data_frame, col = 'Sex')
g.map(plt.hist, 'Age') #Fazendo pelo Matplotlib
plt.show()