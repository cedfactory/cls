import os
import pandas as pd

def wipe_out_directory(path):
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

def clean_up_df_symbol(path):
    df = pd.read_csv(path)
    df = drop_df_duplicates(df, "symbol")
    for c in df.columns:
        if c.startswith("Unnamed"):
            df.drop(c, axis=1, inplace=True)

    df.to_csv(path)

