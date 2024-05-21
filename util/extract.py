import pandas as pd


def extract_csv(ano: int, etapa: str, semestre: int) -> pd.DataFrame:
    """extrai arquivo csv de sisu de acordo com os argumentos

    Args:
        ano (int): 2017 a 2022
        etapa (str): lista_de_espera ou chamada_regular
        semestre (int): 1 ou 2
    """
    arquivo_nome = f"{etapa}_sisu_{ano}_{semestre}"
    # Set the chunk size
    chunk_size = 100000

    # Initialize an empty dataframe
    df = pd.DataFrame()
    
    try:
        for chunk in pd.read_csv(
            f"sisu/{ano}/{arquivo_nome}.csv", sep=";", encoding="utf-8", chunksize=chunk_size
        ):
            df = df.append(chunk, ignore_index=True)
        return df
    except Exception as e:
        print(e)
        for chunk in  pd.read_csv(
            f"sisu/{ano}/{arquivo_nome}.csv", sep="|", encoding="ISO-8859-1", chunksize=chunk_size
        ):
            df = df.append(chunk, ignore_index=True)
        return df
