import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data_frame = pd.read_csv('Titanic-Dataset.csv')

sns.set_style('whitegrid')
print(data_frame.info())

#24
sns.jointplot(x = 'Fare', y = 'Age', data = data_frame)
plt.show