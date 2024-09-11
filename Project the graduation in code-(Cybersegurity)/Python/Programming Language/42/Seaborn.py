
#1


import seaborn as sns

import matplotlib.pyplot as plt

 

sns.set(style=“whitegrid”)

 

df = sns.load_dataset('tips')

 

plt.figure(figsize=(8, 5))

sns.barplot(x='time', y='total_bill', data=df, estimator=sum, ci=None, palette=“Set2”)

plt.xlabel('Período (Time)')

plt.ylabel('Total de Gastos')

plt.title('Total de Gastos por Período (Almoço ou Jantar)')

plt.show() 



#2

plt.figure(figsize=(8, 5))

sns.barplot(x='time', y='total_bill', data=df)#, #estimator=sum, ci=None, palette=“Set2”)

plt.xlabel('Período (Time)')

plt.ylabel('Média de Gastos')

plt.title('Média de Gastos por Período (Almoço ou Jantar)')

plt.show()
