import config

from tools import save_list

from scrap_wiki_list import get_list_CAC
from scrap_wiki_list import get_list_DAX
from scrap_wiki_list import get_list_NASDAQ100
from scrap_wiki_list import get_list_DJI
from scrap_wiki_list import get_list_SP500
from scrap_yahoo_list import get_list_EURONEXT
from scrap_yahoo_list import get_list_YAHOO
from scrap_yahoo_list import get_list_NASDAQ
from scrap_yahoo_list import get_list_DOW
from scrap_yahoo_list import get_list_yahoo_SP500
from scrap_yahoo_list import get_list_FTSE100
from scrap_yahoo_list import get_list_FTSE250
from scrap_yahoo_list import get_list_IBOVESPA
from scrap_yahoo_list import get_list_NIFTY50
from scrap_yahoo_list import get_list_NIFTY_BANK

def get_list():
    if(config.GET_EURONEXT == True):
        df_EURONEXT = get_list_EURONEXT()
        save_list(df_EURONEXT, config.OUTPUT_DIR_EUROPE, "EURONEXT.csv")

    if(config.GET_CAC == True):
        df_CAC = get_list_CAC()
        save_list(df_CAC, config.OUTPUT_DIR_EUROPE, "CAC_40.csv")

    if(config.GET_DAX == True):
        df_DAX = get_list_DAX()
        save_list(df_DAX, config.OUTPUT_DIR_EUROPE, "DAX.csv")

    if(config.GET_FTSE == True):
        df_FTSE = get_list_FTSE100()
        save_list(df_FTSE, config.OUTPUT_DIR_EUROPE, "FTSE100.csv")
        df_FTSE = get_list_FTSE250()
        save_list(df_FTSE, config.OUTPUT_DIR_EUROPE, "FTSE250.csv")

    if (config.GET_NASDAQ100 == True):
        df_NASDAQ100 = get_list_NASDAQ100()
        save_list(df_NASDAQ100, config.OUTPUT_DIR_US, "NASDAQ100.csv")

    if (config.GET_NASDAQ == True):
        df_NASDAQ = get_list_NASDAQ()
        save_list(df_NASDAQ, config.OUTPUT_DIR_US, "NASDAQ.csv")

    if (config.GET_DJI == True):
        df_DJI = get_list_DJI()
        save_list(df_DJI, config.OUTPUT_DIR_US, "DJI.csv")
        df_DJI = get_list_DOW()
        save_list(df_DJI, config.OUTPUT_DIR_US, "DOW.csv")

    if (config.GET_SP500 == True):
        df_SP500 = get_list_SP500()
        save_list(df_SP500, config.OUTPUT_DIR_US, "SP500.csv")
        df_SP500 = get_list_yahoo_SP500()
        save_list(df_SP500, config.OUTPUT_DIR_US, "SP500_y.csv")

    if (config.GET_YAHOO == True):
        df_actives, df_trending, df_gainers, df_loosers, df_undervaluated = get_list_YAHOO()
        save_list(df_actives, config.OUTPUT_DIR_OTHERS, "ACTIVES.csv")
        save_list(df_trending, config.OUTPUT_DIR_OTHERS, "TRENDING.csv")
        save_list(df_gainers, config.OUTPUT_DIR_OTHERS, "GAINERS.csv")
        save_list(df_loosers, config.OUTPUT_DIR_OTHERS, "LOOSERS.csv")
        save_list(df_undervaluated, config.OUTPUT_DIR_OTHERS, "UNDERVALUATED.csv")

    if (config.GET_IBOVESPA == True):
        df_IBOVESPA = get_list_IBOVESPA()
        save_list(df_IBOVESPA, config.OUTPUT_DIR_OTHERS, "IBOVESPA.csv")

    if (config.GET_NIFTY == True):
        df_NIFTY = get_list_NIFTY50()
        save_list(df_NIFTY, config.OUTPUT_DIR_OTHERS, "NIFTY50.csv")
        df_NIFTY = get_list_NIFTY_BANK()
        save_list(df_NIFTY, config.OUTPUT_DIR_OTHERS, "NIFTYBANK.csv")