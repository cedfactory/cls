import pandas as pd
from init import config
from scraping import scrap_wiki_list

'''
symbol_list_filename_in is rewritten except if symbol_list_filename_out is specified
'''
def fill_df(symbol_list_filename_in, symbol_list_isni_filename_out,
            symbol_list_filename_out=""):
    if symbol_list_filename_out == "":
        symbol_list_filename_out = symbol_list_filename_in
    df = pd.read_csv(symbol_list_filename_in)
    
    df = df.set_index('symbol', drop=True)
    df.drop("Unnamed: 0", axis=1, inplace=True)

    df_data = pd.read_csv(config.INPUT_FILE_IMPORTED_DATA)
    df_data = df_data.set_index('symbol', drop=True)

    df_isni_data = pd.read_csv(config.INPUT_FILE_IMPORTED_DATA_ISNI)
    df_isni_data = df_isni_data.set_index('symbol', drop=True)
    df_isni_data.drop("Unnamed: 0", axis=1, inplace=True)

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

    list_stock_dropped = []
    empty_lst = []
    df_isni = scrap_wiki_list.make_df_stock_info(empty_lst, empty_lst, empty_lst, empty_lst, empty_lst, empty_lst, empty_lst)
    for stock in list_stock_no_data:
        try:
            row_df_isni = df_isni_data.index.get_loc(df_isni_data.index[df_isni_data.index == stock][0])
            df_isni = df_isni.append(df_isni_data.iloc[row_df_isni])
        except:
            # print('no data: ', stock)
            list_stock_dropped.append(stock)
    df_isni['symbol'] = df_isni.index
    df_isni.reset_index(drop=True, inplace=True)


    print("symbols with data: ", len(df), " => ", symbol_list_filename_out)
    print("symbols with ISNI: ", len(df_isni), " => ", symbol_list_isni_filename_out)
    print("dropped symbols:   ", len(list_stock_dropped), " =>  Get the fuck out")
    # print(list_stock_no_data)

    df.to_csv(symbol_list_filename_out)
    df_isni.to_csv(symbol_list_isni_filename_out)
