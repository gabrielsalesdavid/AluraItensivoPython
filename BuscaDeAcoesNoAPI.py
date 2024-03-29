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

# definição de layout do grafico candles.
width = 0.7

# laço de repetição para o grafico candles.
for i in range(len(df)):
    # estrutura de condições composta.
    # se uma coluna declarda entre colchete for maior do que a outra, o comando retorna a cor verde no candles.
    # do contrario vermelho.
    if df['coluna'].iloc[i] > df['coluna'].iloc[i]:
        color = 'green'
    else:
        color = 'red'

    # define o ponto x e y da data em uma linha.
    # define uma linha no valor minnimo e maximo.
    ax.plot([df['Data'].iloc[i], df['Data'].iloc[i]],
            [df['Minimo'].iloc[i], df['Maximo'].iloc[i]],
            color = color, linewidth = 1)

    # passa a cor da linha
    ax.add_patch(plt.Rectangle((df['Data'].iloc[i] - width / 2, min(df['Abertura'].iloc[i], df['fechamento'].iloc[i])),
                               width, abs(df['fechamento'].iloc[i] - df['Abertura'].iloc[i]), facecolor = color))