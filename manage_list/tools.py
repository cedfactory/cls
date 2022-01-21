import os
import pandas as pd
from init import config

def save_list(df, path, filename):
    filename = path + filename
    df.to_csv(filename)

def mk_directories():
    if not os.path.exists(config.OUTPUT_DIR):
        os.makedirs(config.OUTPUT_DIR)
    if not os.path.exists(config.OUTPUT_DIR_DATE):
        os.makedirs(config.OUTPUT_DIR_DATE)
    if not os.path.exists(config.OUTPUT_DIR_MERGED):
        os.makedirs(config.OUTPUT_DIR_MERGED)
    if not os.path.exists(config.OUTPUT_DIR_RESULT):
        os.makedirs(config.OUTPUT_DIR_RESULT)
    if not os.path.exists(config.OUTPUT_DIR_MARKET):
        os.makedirs(config.OUTPUT_DIR_MARKET)
    if not os.path.exists(config.OUTPUT_DIR_EUROPE):
        os.makedirs(config.OUTPUT_DIR_EUROPE)
    if not os.path.exists(config.OUTPUT_DIR_US):
        os.makedirs(config.OUTPUT_DIR_US)
    if not os.path.exists(config.OUTPUT_DIR_ASIA):
        os.makedirs(config.OUTPUT_DIR_ASIA)
    if not os.path.exists(config.OUTPUT_DIR_OTHERS):
        os.makedirs(config.OUTPUT_DIR_OTHERS)

def wipe_out_directory(path):
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))

def get_input_list(file):
    df_input = pd.read_csv(config.INPUT_DIR + file)
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

