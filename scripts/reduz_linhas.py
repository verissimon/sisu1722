### Script para reduzir o número de linhas de um arquivo CSV
# util para testar o código em um arquivo menor
import pathlib
import random

random.seed(42)

ANO = "2022"
FILE = f'chamada_regular_sisu_{ANO}_1.csv'

PATH = pathlib.Path(__file__).parent.absolute().parent
original_file_path = PATH / 'sisu' / ANO / FILE
new_file_path = PATH / 'reduzido' / f'reduzido_{FILE}'
print(new_file_path)
num_lines_to_sample = 1001

sampled_lines = []

with open(original_file_path, 'r', encoding='iso-8859-1') as original_file:
    first_line = original_file.readline()
    sampled_lines.append(first_line)
    remaining_lines = original_file.readlines()

sampled_lines.extend(random.sample(remaining_lines, num_lines_to_sample - 1))

with open(new_file_path, 'w') as new_file:
    new_file.writelines(sampled_lines)
