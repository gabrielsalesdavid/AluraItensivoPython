import pandas as pd

# df(DataFrame)Principal seria a aba da planilha do excel.
# que esta sendo atribuida com valores para a variavel que caminha e busca o arquivo.
dfPrincipal = pd.read_excel("caminho do arquivo. nome do arquivo em excel", sheet_name = "Nome da aba do excel")
dfPrincipal.head("Intervalo de linha que queira mostrar da planilha")

