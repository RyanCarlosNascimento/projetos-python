import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data_frame = pd.read_csv('Titanic-Dataset.csv')

sns.countplot(x = 'Sex', data = data_frame)
# Count já é um indicativo de histograma -> Ele é feio.
# Proporção, não dá o valor exato.