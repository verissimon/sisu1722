from typing import List
import pandas as pd
from sqlalchemy import Engine
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent


def extract_csv(ano: int, etapa: str, semestre: int) -> pd.DataFrame:
    """extrai arquivo csv de sisu de acordo com os argumentos

    Args:
        ano (int): 2017 a 2022
        etapa (str): lista_de_espera ou chamada_regular
        semestre (int): 1 ou 2
    """
    arquivo_nome = f"{etapa}_sisu_{ano}_{semestre}"
    chunk_size = 100000

    df = pd.DataFrame()

    try:
        for chunk in pd.read_csv(
            ROOT_PATH / "sisu" / str(ano) / f"{arquivo_nome}.csv",
            sep=";",
            encoding="utf-8",
            chunksize=chunk_size,
        ):
            df = pd.concat([df, chunk])
        return df
    except Exception as e:
        print(e)
        for chunk in pd.read_csv(
            ROOT_PATH / "sisu" / str(ano) / f"{arquivo_nome}.csv",
            sep="|",
            encoding="ISO-8859-1",
            chunksize=chunk_size,
        ):
            df = pd.concat([df, chunk])
        return df


def df_concat_queries(tabelas: List[str], query: str, engine: Engine) -> pd.DataFrame:
    """concatena tabelas de acordo com a query

    Args:
        tabelas (List[str]): lista de nomes das tabelas
        query (str): query para definir dataframes que serão concatenados
        engine (Engine): conexão com banco de dados
    Returns:
        pd.DataFrame: dataframe com tabelas concatenadas
    """
    df = pd.DataFrame()
    for tabela in tabelas:
        query_copy = query[:]
        df_tabela = pd.read_sql_query(
            query_copy.format(tabela=tabela),
            engine,
        )
        df = pd.concat([df, df_tabela])
    return df


def extract_df_from_csv_path(path: Path) -> pd.DataFrame:
    """extrai arquivo csv de sisu de acordo com o caminho

    Args:
        path (Path): caminho do arquivo
    """
    chunk_size = 100000

    df = pd.DataFrame()

    try:
        for chunk in pd.read_csv(path, sep="|", encoding="utf-8", chunksize=chunk_size):
            # df = df.append(chunk, ignore_index=True)
            df = pd.concat([df, chunk])
        return df
    except Exception as e:
        print(e)
        return None


def to_csv_with_chunks(df: pd.DataFrame, csv_parent_path: Path, ano: int):
    """escreve um arquivo csv em chunks

    Args:
        df (pd.DataFrame): dataframe a ser escrito
        csv_parent_path (Path): caminho do arquivo
        ano (int): ano do sisu
    """
    chunk_size = 100000
    csv_file = csv_parent_path / f"chamada_regular_sisu_{ano}_1_com_regiao.csv"

    chunks = [df[i : i + chunk_size] for i in range(0, df.shape[0], chunk_size)]

    for i, chunk in enumerate(chunks):
        if i == 0:
            chunk.to_csv(csv_file, sep="|", encoding="utf-8", index=False)
        else:
            chunk.to_csv(
                csv_file, mode="a", sep="|", encoding="utf-8", index=False, header=False
            )
