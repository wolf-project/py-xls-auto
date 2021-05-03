# Generator Script for excel files 
# Testing ...


import pandas as pd
import numpy as np

#Ferramenta que cria gráficos após tratar os dados em tabela de um arquivo
# import matploitlib.pyplot as plt

# Definindo a variável com o arquivo Excel a ser utilizado
excel_archive_1 = 'data_science.xlsx'

# Definindo a leitura do arquivo excel
df_complete_1 = pd.read_excel(excel_archive_1,sheet_name='testing')

print(df_complete_1)



