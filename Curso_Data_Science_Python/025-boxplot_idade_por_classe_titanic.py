import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data_frame = pd.read_csv('Titanic-Dataset.csv')
sns.boxplot(x = 'Pclass', y = 'Age', data= data_frame)
plt.show()