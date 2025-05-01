import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
df = pd.read_csv('campeoes_lol.csv')

# Contar campeões por função
funcoes = df['Função Primária'].value_counts()
print("Campeões por função:\n", funcoes)

# Contar campeões por tipo de dano
dano = df['Dano Principal'].value_counts()
print("\nCampeões por tipo de dano:\n", dano)

# Média de ano de lançamento por função
media_ano = df.groupby('Função Primária')['Ano de Lançamento'].mean()
print("\nMédia do ano de lançamento por função:\n", media_ano)

# Gráfico: Campeões por tipo de dano
dano.plot(kind='bar', title='Campeões por Tipo de Dano', color='skyblue')
plt.xlabel('Tipo de Dano')
plt.ylabel('Quantidade de Campeões')
plt.tight_layout()
plt.savefig('grafico_dano.png')
plt.show()
