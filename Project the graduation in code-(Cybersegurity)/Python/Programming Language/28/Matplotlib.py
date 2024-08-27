
#1

import matplotlib.pyplot as plt

 

# Dados

x = [1, 2, 3, 4, 5]

y = [2, 4, 1, 3, 5]

 

# Criar um gráfico de linha

plt.plot(x, y)

 

# Adicionar rótulos aos eixos

plt.xlabel('Eixo X')

plt.ylabel('Eixo Y')

 

# Adicionar um título ao gráfico

plt.title('Exemplo de Gráfico de Linha')

 

# Mostrar o gráfico

plt.show()


#2 


import matplotlib.pyplot as plt

 

# Dados de exemplo

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']

vendas = [120, 90, 150, 80, 200]

 

# Criar um gráfico de barras

plt.bar(meses, vendas, color='royalblue')

 

# Adicionar rótulos aos eixos

plt.xlabel('Mês')

plt.ylabel('Vendas (em unidades)')

 

# Adicionar um título ao gráfico

plt.title('Vendas Mensais')

 

# Mostrar o gráfico

plt.show()



