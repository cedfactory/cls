import os
import pandas as pd
from init import config

def save_list(df, path, filename):
    filename = path + filename
    df.to_csv(filename)

def mk_directories():
    ALL_DIRS = [config.OUTPUT_DIR, config.OUTPUT_DIR_DATE, config.OUTPUT_DIR_MERGED,
        config.OUTPUT_DIR_RESULT, config.OUTPUT_DIR_MARKET, config.OUTPUT_DIR_EUROPE,
        config.OUTPUT_DIR_US, config.OUTPUT_DIR_ASIA, config.OUTPUT_DIR_OTHERS]
    for dir in ALL_DIRS:
        if not os.path.exists(dir):
            os.makedirs(dir)

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

