import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def pretty_print(name, to_print):
    print(f'{name:}')
    print(f'{to_print}\n\n')

insurance = pd.read_csv("insurance.csv",sep=',',header=0)
print(insurance)
print(insurance.describe())
print(insurance.corr().to_string())

print(insurance.columns)

os.makedirs('plots', exist_ok=True)

# Plotting line chart

plt.plot(insurance['age'],color='red')
plt.title('age')
plt.ylabel('age')
plt.savefig(f'plots/age_plot.png', format='png')
plt.clf()

plt.plot(insurance['charges'],color='pink')
plt.title('charges')
plt.ylabel('charges')
plt.savefig('plots/charges_plot.png', format='png')
plt.clf()

# Plotting Histograms
plt.hist(insurance['bmi'], bins=3, color='yellow')
plt.title('bmi')
plt.xlabel('bmi')
plt.ylabel('bmi')
plt.savefig('plots/bmi_hist.png', format='png')
plt.clf()

# Plotting Scatterplot
plt.scatter(insurance['age'], insurance['charges'], color='b')
plt.title('age to charges')
plt.xlabel('age')
plt.ylabel('charges')
plt.savefig('plots/age_charge_scatter.png', format='png')
plt.clf()

print(insurance[['age','charges']].corr())

# The correlation is 0.299008. The plot matches what we saw.