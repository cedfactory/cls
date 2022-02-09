import pandas as pd
from yahoo_fin import stock_info as si
import yfinance as yf

from init import config

def get_info_list(df):
    list_stocks = df['symbol'].to_list()
    list_failed_stock = []
    df = df.set_index('symbol',drop=True)

    for stock in list_stocks:
        get_data_success = True
        try:
            yf_stock = yf.Ticker(stock)
            df.loc[stock, 'isin'] = yf_stock.isin
            # print(df.loc[stock, 'isin'])
            df.loc[stock, 'industry'] = yf_stock.info['industry']
            df.loc[stock, 'sector'] = yf_stock.info['sector']
            df.loc[stock, 'name'] = yf_stock.info['shortName']
            df.loc[stock, 'country'] = yf_stock.info['country']
            df.loc[stock, 'exchange'] = yf_stock.info['exchange']

            # print('get yahoo data stock: ', stock)
            # quote_data = si.get_quote_data(stock)
            # exchange = quote_data['fullExchangeName']
        except:
            print('error yahoo data stock: ',stock)
            get_data_success = False
            # df.drop([stock], inplace=True)
            list_failed_stock.append(stock)

    df_failed = pd.DataFrame({'symbol': list_failed_stock})

    return df, df_failed


def refresh_database(input_file):
    df = pd.read_csv(config.OUTPUT_DIR_RESULT + 'symbol_list_' + input_file + '.csv')

    df_with_info, df_failed = get_info_list(df)

    df_with_info.to_csv(config.OUTPUT_DIR_RESULT + input_file + '_with_info.csv')
    df_failed.to_csv(config.OUTPUT_DIR_RESULT + input_file + '_failed.csv')

