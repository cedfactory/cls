import numpy as np
import pandas as pd
from init import config
import concurrent.futures
from scraping import scrap_wiki_list
from merging import merging_csv
from manage_list import tools
from manage_list import cross_check
from scraping import scrap_profile
'''
symbol_list_filename_in is rewritten except if symbol_list_filename_out is specified
'''
def fill_df(symbol_list_filename_in, symbol_list_filename_out):
    if symbol_list_filename_out == "":
        symbol_list_filename_out = symbol_list_filename_in
    df = pd.read_csv(symbol_list_filename_in)
    df = df.set_index('symbol', drop=True)
    df = tools.clean_up_df_column(df)

    # DEBUG
    # df = df[:30]

    len_list = len(df)

    df_data = pd.read_csv(config.INPUT_FILE_IMPORTED_DATA)
    df_data = df_data.set_index('symbol', drop=True)
    df_data = tools.clean_up_df_column(df_data)

    list_stock_no_data = []
    for stock in df.index.tolist():
        try:
            row_df_stock = df.index.get_loc(df.index[df.index == stock][0])
            row_df_data_stock = df_data.index.get_loc(df_data.index[df_data.index == stock][0])
            df.loc[df.index[row_df_stock]] = df_data.iloc[row_df_data_stock]
        except:
            # print('no data: ', stock)
            df.drop(stock, inplace=True)
            list_stock_no_data.append(stock)

    empty_lst = [np.nan] * len(list_stock_no_data)
    df_no_data = scrap_wiki_list.make_df_stock_info(list_stock_no_data, empty_lst, empty_lst, empty_lst, empty_lst, empty_lst, empty_lst)

    if (config.MULTITHREADING == True):
        global_split_list = tools.split_list_into_list(df_no_data, config.MULTITHREADING_NB_SPLIT_DF)

        with concurrent.futures.ThreadPoolExecutor(max_workers=config.MULTITHREADING_NUM_THREADS) as executor:
            executor.map(scrap_profile.get_info_multi_list, global_split_list)
        df_with_info = merging_csv.merge_csv_to_df(config.MULTITHREADING_POOL, "*_result.csv")
        df_failed = merging_csv.merge_csv_to_df(config.MULTITHREADING_POOL, "*_failed.csv")
    else:
        df_with_info, df_failed = scrap_profile.get_info_list(df)

    df_with_info = cross_check.check_valid_data(df_with_info)

    if len(df_with_info) > 0:
        df_database = pd.read_csv(config.INPUT_FILE_IMPORTED_DATA)
        df_database = tools.concat_and_clean_df(df_database, df_with_info, 'symbol')
        print('DATABASE UPDATED WITH: ', len(df_with_info), " SYMBOLS => ", config.INPUT_FILE_IMPORTED_DATA)
        df_database.to_csv(config.INPUT_FILE_IMPORTED_DATA)

    df = tools.concat_and_clean_df(df, df_with_info, 'symbol')

    print("SYMBOLS WITH DATA: ", len(df), " => ", symbol_list_filename_out)
    print("TOTAL SYMBOLS DROPPED:   ", len_list - len(df), " =>  Get the fuck out")

    df.to_csv(symbol_list_filename_out)
