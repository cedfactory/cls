import pandas as pd
#from yahoo_fin import stock_info as si
import yfinance as yf
import concurrent.futures
import uuid
from merging import merging_csv
from manage_list import tools
from init import config

def get_info_list(df):
    list_stocks = df['symbol'].to_list()
    list_failed_stock = []
    df = df.set_index('symbol',drop=True)

    for stock in list_stocks:
        get_data_success = True
        try:
            yf_stock = yf.Ticker(stock)
            try:
                df.loc[stock, 'isin'] = yf_stock.isin
            except:
                pass
            try:
                df.loc[stock, 'industry'] = yf_stock.info['industry']
            except:
                pass
            try:
                df.loc[stock, 'sector'] = yf_stock.info['sector']
            except:
                pass
            try:
                df.loc[stock, 'name'] = yf_stock.info['shortName']
            except:
                pass
            try:
                df.loc[stock, 'country'] = yf_stock.info['country']
            except:
                pass
            try:
                df.loc[stock, 'exchange'] = yf_stock.info['exchange']
            except:
                pass
            # print('get yahoo data stock: ', stock)
            # quote_data = si.get_quote_data(stock)
            # exchange = quote_data['fullExchangeName']
        except:
            print('error yahoo data stock: ',stock)
            # get_data_success = False
            # df.drop([stock], inplace=True)
            list_failed_stock.append(stock)

    df_failed = pd.DataFrame({'symbol': list_failed_stock})
    df['symbol'] = df.index
    df.reset_index(drop=True, inplace=True)
    df = tools.move_column_position(df, 'symbol', 0)
    df = tools.clean_up_df_column(df)

    return df, df_failed

def get_info_multi_list(df):
    df_with_info, df_failed = get_info_list(df)
    filename_info = config.MULTITHREADING_POOL + str(uuid.uuid4()) + '_result.csv'
    filename_failed = config.MULTITHREADING_POOL + str(uuid.uuid4()) + '_failed.csv'
    df_with_info.to_csv(filename_info)
    df_failed.to_csv(filename_failed)

def refresh_database(input_file):
    list_df_result = []
    df = pd.read_csv(config.OUTPUT_DIR_RESULT + 'symbol_list_' + input_file + '.csv')

    # DEBUG
    df = df[:30]

    if (config.MULTITHREADING == True):
        global_split_list = tools.split_list_into_list(df, config.MULTITHREADING_NB_SPLIT_DF)

        with concurrent.futures.ThreadPoolExecutor(max_workers=config.MULTITHREADING_NUM_THREADS) as executor:
            executor.map(get_info_multi_list, global_split_list)
        df_with_info = merging_csv.merge_csv_to_df(config.MULTITHREADING_POOL, "*_result.csv")
        df_failed = merging_csv.merge_csv_to_df(config.MULTITHREADING_POOL, "*_failed.csv")
    else:
        df_with_info, df_failed = get_info_list(df)

    df_with_info.to_csv(config.OUTPUT_DIR_RESULT + input_file + '_with_info.csv')
    df_failed.to_csv(config.OUTPUT_DIR_RESULT + input_file + '_failed.csv')

