### Script para reduzir o número de linhas de um arquivo CSV
# util para testar o código em um arquivo menor

import random

random.seed(42)

ANO = "2017"
FILE = f'chamada_regular_sisu_{ANO}_2.csv'

original_file_path = f'./sisu/{ANO}/{FILE}'

new_file_path = f'./reduzido/{ANO}/reduzido_{FILE}'

num_lines_to_sample = 1000

sampled_lines = []

with open(original_file_path, 'r', encoding='utf-8') as original_file:
    first_line = original_file.readline()
    sampled_lines.append(first_line)
    remaining_lines = original_file.readlines()


sampled_lines.extend(random.sample(remaining_lines, num_lines_to_sample - 1))  # Subtract 1 for the first line

with open(new_file_path, 'w') as new_file:
    new_file.writelines(sampled_lines)
