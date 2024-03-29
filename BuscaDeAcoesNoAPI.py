import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# criação de grafico.
fig = px.bar(dfAnaliseSaldo, x = 'coluna', y = 'coluna', text = 'coluna', title = 'titulo')
fig.show()

# consulta no API as ações declarada/parametrizada por periodo.
dados = yf.download('PETR4.SA', start = '2023-01-01', end = '2023-12-31')
dados

# visualizar as colunas e renomeia.
dados.columns = ['coluna', 'que', 'deseja', 'renomear']
dados

# renomeia a função.
dados.rename_axis('Data')
dados

# criação de grafico.
dados['coluna'].plot(figsize = (10,6))

# titulo no grafico.
plt.title('Nome do titulo!', fontsize = 16)
plt.legend['Nome do grafico']

# copia o cabeçalho e transforma indice em uma coluna com a quantidade de linhas parametrizada.
df = dados.head(60).copy()
df['Data'] = df.index

# converte as datas para um formato numerico em que o matplotlib possa plotar as datas corretamentes no grafico.
df['Data'] = df['Data'].apply(mdates.date2num)

# Crição da tela preferencial com altura e largura.
fig, ax = plt.subplots(figsize =  (15, 8))

