import pandas as pd
import config

import investpy

def get_data_from_ISIN():

    df_data = pd.read_csv(config.INPUT_FILE_IMPORTED_DATA)
    df_data = df_data.set_index('symbol', drop=True)
    df_data.drop("Unnamed: 0", axis=1, inplace=True)

    df_isni_data = pd.read_csv(config.INPUT_FILE_IMPORTED_DATA_ISNI)
    df_isni_data = df_isni_data.set_index('isin', drop=True)
    df_isni_data.drop("Unnamed: 0", axis=1, inplace=True)

    for insi_nb in  df_isni_data.index.tolist():
        df_insi = investpy.stocks.search_stocks(by='isin', value=insi_nb)
        print(df_insi)
        print(df_isni_data['country'][insi_nb])



