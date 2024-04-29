etapa = "chamada_regular"
# etapa = "lista_de_espera"
ano = 2020
semestre = 2
arquivo_nome = f"{etapa}_sisu_{ano}_{semestre}"
arquivo_path = f'./sisu/{ano}/{arquivo_nome}.csv'
transformado_path = f'./transformado/{ano}/{arquivo_nome}.csv'
nome_tabela = arquivo_nome.replace('sisu_', '').replace('de_', '')

