import os
import pandas as pd
import numpy as np

def wipe_out_directory(path):
    if os.path.isdir(path) == True:
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))

def get_input_list(file):
    df_input = pd.read_csv(file)
    df_input = df_input.set_index('files')

    list_files = []
    for f in df_input.index:
        if df_input.loc[f, 'merge'] == True:
            list_files.append(f+'.csv')
    return list_files

def drop_df_duplicates(df, column):
    len_df = len(df)
    # dropping ALL duplicate values
    df.sort_values(by=[column], inplace=True)
    df.drop_duplicates([column], keep='first',inplace=True)
    df.reset_index(drop=True, inplace=True)
    if(len_df - len(df) > 0):
        print("total tickers nb:      ", len_df)
        print("-> duplicates removed: ", len_df - len(df))
        print("-> remaining symbols:  ", len(df))
        print("")
    return df

def set_euronext_data_symbol(df):
    df["newsymbol"] = ""
    tickers = df['symbol'].tolist()
    # insert_df_column(df)
    df = df.set_index('symbol')
    for ticker in tickers:
        if df.market[ticker].endswith("Paris"):
            df["newsymbol"][ticker] = ticker + ".PA"
        elif df.market[ticker].endswith("Brussels"):
            df["newsymbol"][ticker] = ticker + ".BE"
        elif df.market[ticker].endswith("Amsterdam"):
            df["newsymbol"][ticker] = ticker + ".AS"
        elif df.market[ticker].endswith("Dublin"):
            df["newsymbol"][ticker] = ticker + ".IR"
        elif df.market[ticker].endswith("Lisbon"):
            df["newsymbol"][ticker] = ticker + ".LS"
        elif df.market[ticker].endswith("Oslo"):
            df["newsymbol"][ticker] = ticker + ".OL"

    df['newsymbol'].replace('', np.nan, inplace=True)
    df.dropna(subset=["newsymbol"], inplace=True)

    # df['symbol'] = df.index
    df.reset_index(drop=True, inplace=True)

    first_column = df.pop('newsymbol')
    df.insert(0, 'symbol', first_column)

    return df

def clean_up_df_symbol(path_in, path_out=""):
    if path_out == "":
        path_out = path_in
    df = pd.read_csv(path_in)
    df = drop_df_duplicates(df, "symbol")
    for c in df.columns:
        if c.startswith("Unnamed"):
            df.drop(c, axis=1, inplace=True)

    if "euronext" in path_in.lower():
        df = set_euronext_data_symbol(df)

    df.to_csv(path_out)

