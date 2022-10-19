import pandas as pd
import numpy as np
import nltk
import json


def DevolverFilas(File):

    df = pd.read_csv(File, sep=';', encoding="utf-8")

    cabecera = df.columns.tolist()

    df = pd.DataFrame(cabecera)

    json = df.to_json()

    file=File(file_name=File, classification='csv', status="pross", datetime="data_string")
    file.save()

    return json


