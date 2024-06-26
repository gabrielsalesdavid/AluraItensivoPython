import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# df(DataFrame)Principal seria a aba da planilha do excel.
# que esta sendo atribuida com valores para a variavel que caminha e busca o arquivo.
dfPrincipal = pd.read_excel("caminho do arquivo. nome do arquivo em excel", sheet_name = "Nome da aba do excel")
dfPrincipal.head("Intervalo de linha que queira mostrar da planilha")

# entre os colhetes duplo são a inserção de dados de coluna do excel que se desejamos que seja inserido de acordo
# a nossa usabilidade.
# python copia e retorna as colunas desejadas inseridos nos colchetes e separada por virgulas.
dfPrincipal = dfPrincipal[['Colunas que desejamos que seja inserido para que haja muitos dados']].copy()
dfPrincipal

# o df recebendo ele mesmo para renomear as colunas desejadas entre as chaves com o valor inicial : final.
# alteração de descrição das colunas em python.
dfPrincipal = dfPrincipal.rename(columns = {"mudar os titulos das colunas que seja alteradas"}).copy()
dfPrincipal

# python cira/insere uma coluna que calcula os dados de uma outra que se deseja calcular.
dfPrincipal['cirar uma coluna no excel'] = dfPrincipal['inserção de dados da coluna'] / 100
dfPrincipal['criar uma coluna'] = dfPrincipal['inserir uma coluna'] / (dfPrincipal['coluna que deseja calcular'] + 1)
dfPrincipal

# python busca uma aba da planilha e passa os parametros para o que se deseja inserir ou buscar.
# left_on seleciona a aba que se deseja buscar os dados.
# how diz para o python a principal coluna. merge mescla os dados. Ou seja, um porcV ou vlookUp.
dfPrincipal = dfPrincipal.merge(dfTotalAcoes, left_on = 'A coluna que se deseja buscar os dados', how = 'left')
dfPrincipal

# remove a coluna que e desejada.
dfPrincipal = dfPrincipal.drop(columns = ['remover a coluna que se deseja'])
dfPrincipal

# criação dde nova coluna e a inserção de calculos das outras.
dfPrincipal['criacao de uma coluna'] = (dfPrincipal['coluna'] - dfPrincipal['coluna']) * dfPrincipal['coluna']
dfPrincipal

# formatação de duas casas decimais em variavel float, ou seja, ponto flutuante!
pd.options.display.float_format = '{:.2f}'.format

# parametrizando de float para int.
dfPrincipal['coluna'] = dfPrincipal['coluna'].astype(int)

# renomear coluna.
dfPrincipal = dfPrincipal.rename(columns = {'nomeColuna:Coluna'}).copy()
dfPrincipal

# estrutura condicional(if else).
# que retorna dados que teve uma certa variação entre queda e a alta.
dfPrincipal['criar coluna'] = dfPrincipal['coluna principal'].apply(lambda x: 'Subiu' if x > 0 else('Desceu' if x < 0 else 'Estavel'))
dfPrincipal

# mesclar dados de uma coluna/aba.
dfPrincipal = dfPrincipal.merge(dfAba, left_on = 'coluna', right_on = 'Coluna', how = 'left')
dfPrincipal = dfPrincipal.drop(columns = ['coluna/Aba'])
dfPrincipal

# retorna o valor maximo da coluna selecionada.
maior = dfPrincipal['coluna'].max()

# retorna o valor menor da coluna selecionada.
menor = dfPrincipal['coluna'].main()

# retorna o valor da media da coluna selecionada.
media = dfPrincipal['coluna'].mean()

# retorna a media de quem subiu da coluna.
mediaSubiu = dfPrincipal[dfPrincipal['coluna'] == 'mensagem']['coluna'].mean()

# retorna a media de quem desceu da coluna.
mediaDesceu = dfPrincipal[dfPrincipal['coluna'] == 'mensagem']['coluna'].mean()

# saida de dados das variaveis declaradas passando uma formatação.
print(f"Maior\tR$ {maior:, .2f}")
print(f"Menor\tR$ {menor:, .2f}")
print(f"Media\tR$ {media:, .2f}")
print(f"Media de quem subiu\tR$ {mediaSubiu:, .2f}")
print(f"Media de quem desceu\tR$ {mediaDesceu:, .2f}")

# cria uma coluna com dados de media da variação.
dfPrincipalSubiu = dfPrincipal[dfPrincipal['coluna'] == 'mensagem']['coluna']
dfPrincipalSubiu

# retorna uma soma de colunas.
dfAnaliseSegmento = dfPrincipalSubiu.groupby('coluna')['coluna'].sum().reset_index()
dfAnaliseSegmento

# retorna os dados da coluna com uma valor somado de tudo. Ou seja, se subiu, ficou estavel e ou desceu!
dfAnaliseSaldo = dfAnaliseSaldo.groupby('coluna')['coluna'].sum().reset_index()
dfAnaliseSaldo