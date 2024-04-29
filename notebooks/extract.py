import pandas as pd


def extract_csv(ano: int, etapa: str, semestre: int) -> pd.DataFrame:
    """extrai arquivo csv de sisu de acordo com os argumentos

    Args:
        ano (int): 2017 a 2022
        etapa (str): lista_de_espera ou chamada_regular
        semestre (int): 1 ou 2
    """
    arquivo_nome = f"{etapa}_sisu_{ano}_{semestre}"
    try:
        return pd.read_csv(
            f"sisu/{ano}/{arquivo_nome}.csv", sep=";", encoding="utf-8"
        )
    except Exception as e:
        print(e)
        return pd.read_csv(
            f"sisu/{ano}/{arquivo_nome}.csv", sep="|", encoding="ISO-8859-1"
        )
