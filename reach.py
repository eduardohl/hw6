import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def pretty_print(name, to_print):
    print(f'{name:}')
    print(f'{to_print}\n\n')

heart = pd.read_csv("heart.csv",sep=',',header=0)
print(heart)
print(heart.describe())
print(heart.corr().to_string())

print(heart.columns)

os.makedirs('plots2', exist_ok=True)

# Plotting line chart

plt.plot(heart['target'],color='red')
plt.title('target')
plt.ylabel('target')
plt.savefig(f'plots2/target_plot.png', format='png')
plt.clf()

# Plotting Histograms
plt.hist(heart['age'], bins=3, color='yellow')
plt.title('age')
plt.xlabel('age')
plt.ylabel('age')
plt.savefig('plots2/age_hist.png', format='png')
plt.clf()

# Plotting Scatterplot
plt.scatter(heart['chol'], heart['target'], color='b')
plt.title('chol to targeet')
plt.xlabel('chol')
plt.ylabel('target')
plt.savefig('plots2/chol_target_scatter.png', format='png')
plt.close()

plt.scatter(heart['age'], heart['chol'], color='b')
plt.title('age to chol')
plt.xlabel('age')
plt.ylabel('chol')
plt.savefig('plots2/age_chol_scatter.png', format='png')
plt.close()