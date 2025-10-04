import numpy as np
import matplotlib.pyplot as plt
import os

# Garante que o diretório 'graficos' existe
os.makedirs('graficos', exist_ok=True)

# Paleta de cores harmoniosa (tema mata)
cores_mata_hist = ['mediumseagreen', 'burlywood', 'olivedrab']  # Pitfall, Aspirador, Winkler

# 1) Lepidocyrtus sp.n.5
metodos = ['Pitfall', 'Aspirador', 'Winkler']
totais = [13469, 953, 314]
especie = [4562, 20, 2]
prob = [4562/13469, 20/953, 2/314]
n_sim = 10000
simulados = [np.random.binomial(t, p, n_sim) for t, p in zip(totais, prob)]

plt.figure(figsize=(10,3))
for i, m in enumerate(metodos):
    plt.hist(simulados[i], bins=30, alpha=0.7, label=m, color=cores_mata_hist[i])
plt.title('Distribuição simulada de capturas de Lepidocyrtus sp.n.5 por método')
plt.xlabel('Indivíduos capturados')
plt.ylabel('Frequência')
plt.legend()
plt.tight_layout()
plt.savefig('graficos/condicional_lepidocyrtus.png')
plt.close()

# 2) Lepidocyrtinus paraibensis
especie = [2312, 522, 54]
prob = [2312/13469, 522/953, 54/314]
simulados = [np.random.binomial(t, p, n_sim) for t, p in zip(totais, prob)]

plt.figure(figsize=(10,3))
for i, m in enumerate(metodos):
    plt.hist(simulados[i], bins=30, alpha=0.7, label=m, color=cores_mata_hist[i])
plt.title('Distribuição simulada de capturas de Lepidocyrtinus paraibensis por método')
plt.xlabel('Indivíduos capturados')
plt.ylabel('Frequência')
plt.legend()
plt.tight_layout()
plt.savefig('graficos/condicional_paraibensis.png')
plt.close()

# 3) Rhynchocyrtus sp.n.1
especie = [164, 33, 3]
prob = [164/13469, 33/953, 3/314]
simulados = [np.random.binomial(t, p, n_sim) for t, p in zip(totais, prob)]

plt.figure(figsize=(10,3))
for i, m in enumerate(metodos):
    plt.hist(simulados[i], bins=30, alpha=0.7, label=m, color=cores_mata_hist[i])
plt.title('Distribuição simulada de capturas de Rhynchocyrtus sp.n.1 por método')
plt.xlabel('Indivíduos capturados')
plt.ylabel('Frequência')
plt.legend()
plt.tight_layout()
plt.savefig('graficos/condicional_rhynchocyrtus.png')
plt.close()

# 4) Simulação Monte Carlo para planejamento amostral (scatter harmonioso)
n_especies = 43
prob_pitfall = 0.8837
amostras = np.random.binomial(n_especies, prob_pitfall, n_sim)
valores, contagem = np.unique(amostras, return_counts=True)

plt.figure(figsize=(8,4))
scatter = plt.scatter(valores, contagem, c=contagem, cmap='YlGn', s=80, edgecolor='black')
plt.colorbar(scatter, label='Frequência')
plt.title('Distribuição simulada de espécies detectadas pelo Pitfall (Monte Carlo)')
plt.xlabel('Número de espécies detectadas')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('graficos/montecarlo_scatter.png')
plt.close()