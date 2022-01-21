import os, fnmatch
import shutil
import pandas as pd
import config
import datetime
from datetime import date, timedelta

from tools import wipe_out_directory
from tools import get_input_list
from tools import drop_df_duplicates

def merge_csv_to_df(path, pattern):
    current_dir = os.getcwd()
    os.chdir(path)

    listOfFilesToRemove = os.listdir('./')
    #pattern = "*.csv"
    li = []
    for entry in listOfFilesToRemove:
        if fnmatch.fnmatch(entry, pattern):
            print("csv file : ",entry)
            # df = pd.read_csv(entry, index_col=False, header=0)
            df = pd.read_csv(entry, index_col=[0])
            li.append(df)
    df_frame = pd.concat(li, axis=0, ignore_index=True)

    os.chdir(current_dir)

    return df_frame

def merge_list(input_files):
    wipe_out_directory(config.OUTPUT_DIR_MERGED)

    list_files = get_input_list(input_files)
    # print(list_files)

    file_merge_list = []
    for dir in config.OUTPUT_LIST_DIR:
        for f in os.listdir(dir):
            if (f in list_files):
                file_merge_list.append(os.path.join(dir, f))
                shutil.copyfile(os.path.join(dir, f), os.path.join(config.OUTPUT_DIR_MERGED, f))
    # print(file_merge_list)

    df_merged = merge_csv_to_df(config.OUTPUT_DIR_MERGED, '*.csv')
    df_merged = drop_df_duplicates(df_merged, "symbol")

    filename = config.OUTPUT_DIR_RESULT + 'symbol_list_' + input_files
    df_merged.to_csv(filename)


