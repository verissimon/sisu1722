import os
from pathlib import Path


# folder_path = './sisu/2022'
ROOT_PATH = Path(__file__).parent.parent
folder_path = ROOT_PATH / 'transformado' / '2022'
print(os.listdir(folder_path))
# lê primeira linha com colunas de cada csv
com_qt_vagas = []
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            first_line = file.readline()
            print(filename)
            print(first_line, "\n")
            # second_line = file.readline()
            # print(second_line, "\n")
            
            if "QT_VAGAS_CONCORRENCIA" in first_line:
                com_qt_vagas.append(filename)
                
print(com_qt_vagas)

###
# utf-8 sep=";": 
# chamada_regular_sisu_2017_2.csv
# chamada_regular_sisu_2018_2.csv
# chamada_regular_sisu_2019_1.csv
# chamada_regular_sisu_2019_2.csv
# chamada_regular_sisu_2020_1.csv
# chamada_regular_sisu_2020_2.csv
# chamada_regular_sisu_2021_1.csv

# dicionario de dados padronizado
# chamada_regular_sisu_2018_1.csv
# lista_de_espera_sisu_2018_1.csv
# chamada_regular_sisu_2021_2.csv
# lista_de_espera_sisu_2021_2.csv
# lista_de_espera_sisu_2022_1.csv
# lista_de_espera_sisu_2022_2.csv
# chamada_regular_sisu_2022_1.csv
# chamada_regular_sisu_2022_2.csv