# %%
import os
import psycopg2
import csv
import pathlib
# conectar banco de dados

USERNAME = os.environ.get("DB_USERNAME")
PASSWORD = os.environ.get("DB_PASSWORD")
DB_NOME = os.environ.get("DB_NAME")

etapa = "chamada_regular"
# etapa = "lista_de_espera"
ano = 2017
semestre = 1
arquivo_nome = f"{etapa}_sisu_{ano}_{semestre}"
ROOT_PATH = pathlib.Path(__file__).parent.parent
transformado_path = ROOT_PATH / "transformado" / str(ano) / f"{arquivo_nome}.csv"
# transformado_path = f'./transformado/{ano}/{arquivo_nome}.csv'
nome_tabela = arquivo_nome.replace('sisu_', '').replace('de_', '')
print("NOME TABELA", nome_tabela, "\nPATH ALVO: ", transformado_path, "\n")

# %%
conn = psycopg2.connect(
    database=DB_NOME, user=USERNAME, password=PASSWORD, host="localhost", port="5432"
)
cur = conn.cursor()

# tabela tem que ser criada antes

## criar tabela ; utf-8
try:
    with open(transformado_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="|")
        next(reader)
        cur.copy_expert(f"COPY {nome_tabela} FROM STDIN CSV DELIMITER '|' NULL AS ''", f)

    conn.commit()
except Exception as e:
    print(e)
finally:
    cur.close()
    conn.close()


