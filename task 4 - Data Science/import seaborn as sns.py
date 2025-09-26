import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = sns.load_dataset("iris")
sns.pairplot(data, hue="species")
plt.show()
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.show()