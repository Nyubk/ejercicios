import pandas as pd

def convertir_mes(col):
    # Diccionario de traducción
    meses_es_en = {
        'ene': 'jan', 'feb': 'feb', 'mar': 'mar', 'abr': 'apr',
        'may': 'may', 'jun': 'jun', 'jul': 'jul', 'ago': 'aug',
        'sep': 'sep', 'oct': 'oct', 'nov': 'nov', 'dic': 'dec'
    }

    # Reemplazar nombres de mes en español por sus equivalentes en inglés
    col_en = col.str.lower().replace(meses_es_en, regex=True)

    # Convertir a datetime usando formato abreviado en inglés
    return pd.to_datetime(col_en, format='%b-%y')
