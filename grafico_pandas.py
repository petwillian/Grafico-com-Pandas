# -*- coding: utf-8 -*-
"""Grafico_Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zkP5Qo6IFCHtksqmhrm0j0Uq-G7Q7Eok
"""

!pip install --upgrade pip setuptools wheel

!pip install pandas --prefer-binary

!pip freeze > requirements.txt

import pandas as pd

dados = {'Amostra A' : [1, 4, 2, 3], 'Amostra B':[2, 6, 10, 15], 'Amostra C':[4, 12, 20, 26]}
indices = [1, 2, 3, 4]

df = pd.DataFrame(data = dados, index = indices)

df

df.plot.line(title = 'Titulo do Gráfico', ylabel = 'Label Y', xlabel = 'Label X')

"""Gráfico como barras com Pandas"""

import pandas as pd

dados = {'Frutas': ['Laranja', 'Morango', 'Pera', 'Jaca'], 'Quantidades': [60, 100, 85, 30]}

df = pd.DataFrame(data = dados)

df

df.plot.bar(x = 'Frutas', y = 'Quantidades', rot = 0)

"""Histograma com Pandas"""

import pandas as pd
import numpy as np
import matplotlib as plt

pesquisa = np.random.normal(170, 10, 250)

df = pd.DataFrame(data = pesquisa)

plot = df.plot.hist(bins = 8, linewidth = 0.5, edgecolor = '#ffffff', legend = False)

plot.set_ylabel('')

df

"""Gráfico de Pizza com Pandas"""

import pandas as pd
import matplotlib as plt

dados = {'Porcentagem':[15, 30, 45, 10]}
indices = ['Laranja', 'Melancia', 'Manga', 'Jaca']

df = pd.DataFrame(data = dados, index = indices)

#df.plot.pie(subplots = True)# forma 1
df.plot.pie(y = 'Porcentagem', legend = False, autopct = '%1.2f%%').set_ylabel('') #forma 2 set_ylabel tira a legenda

df

"""Salvando Imagens dos gráfico com Pandas"""

import pandas as pd
import matplotlib as plt

dados = {'Porcentagem':[15, 30, 45, 10]}
indices = ['Laranja', 'Melancia', 'Manga', 'Jaca']

df = pd.DataFrame(data = dados, index = indices)

#df.plot.pie(subplots = True)# forma 1
plot = df.plot.pie(y = 'Porcentagem', legend = False, autopct = '%1.2f%%') #forma 2
plot.set_ylabel('')

plot.get_figure().savefig('meu_grafico.png')

# Segundo exemplo

import pandas as pd
import matplotlib as plt

dados = {'Porcentagem':[15, 30, 45, 10]}
indices = ['Laranja', 'Melancia', 'Manga', 'Jaca']

df = pd.DataFrame(data = dados, index = indices)

#df.plot.pie(subplots = True)# forma 1
plot = df.plot.pie(y = 'Porcentagem', legend = False, autopct = '%1.2f%%') #forma 2
plot.set_ylabel('')

plot.get_figure().savefig('meu_grafico2.png', transparent = True, dpi = 150, bbox_inches = 'tight')