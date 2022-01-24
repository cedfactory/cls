from init import config
from manage_list import tools
from scraping import scrap_yahoo_list,scrap_wiki_list

def get_list():
    if(config.GET_EURONEXT == True):
        df_EURONEXT = scrap_yahoo_list.get_list_EURONEXT()
        tools.save_list(df_EURONEXT, config.OUTPUT_DIR_EUROPE, "EURONEXT.csv")

    if(config.GET_CAC == True):
        df_CAC = scrap_wiki_list.get_list_CAC()
        tools.save_list(df_CAC, config.OUTPUT_DIR_EUROPE, "CAC_40.csv")

    if(config.GET_DAX == True):
        df_DAX = scrap_wiki_list.get_list_DAX()
        tools.save_list(df_DAX, config.OUTPUT_DIR_EUROPE, "DAX.csv")

    if(config.GET_FTSE == True):
        df_FTSE = scrap_yahoo_list.get_list_FTSE100()
        tools.save_list(df_FTSE, config.OUTPUT_DIR_EUROPE, "FTSE100.csv")
        df_FTSE = scrap_yahoo_list.get_list_FTSE250()
        tools.save_list(df_FTSE, config.OUTPUT_DIR_EUROPE, "FTSE250.csv")

    if (config.GET_NASDAQ100 == True):
        df_NASDAQ100 = scrap_wiki_list.get_list_NASDAQ100()
        tools.save_list(df_NASDAQ100, config.OUTPUT_DIR_US, "NASDAQ100.csv")

    if (config.GET_NASDAQ == True):
        df_NASDAQ = scrap_yahoo_list.get_list_NASDAQ()
        tools.save_list(df_NASDAQ, config.OUTPUT_DIR_US, "NASDAQ.csv")

    if (config.GET_DJI == True):
        df_DJI = scrap_wiki_list.get_list_DJI()
        tools.save_list(df_DJI, config.OUTPUT_DIR_US, "DJI.csv")
        df_DJI = scrap_yahoo_list.get_list_DOW()
        tools.save_list(df_DJI, config.OUTPUT_DIR_US, "DOW.csv")

    if (config.GET_SP500 == True):
        df_SP500 = scrap_wiki_list.get_list_SP500()
        tools.save_list(df_SP500, config.OUTPUT_DIR_US, "SP500.csv")
        df_SP500 = scrap_yahoo_list.get_list_yahoo_SP500()
        tools.save_list(df_SP500, config.OUTPUT_DIR_US, "SP500_y.csv")

    if (config.GET_YAHOO == True):
        df_actives, df_trending, df_gainers, df_loosers, df_undervaluated = scrap_yahoo_list.get_list_YAHOO()
        tools.save_list(df_actives, config.OUTPUT_DIR_OTHERS, "ACTIVES.csv")
        tools.save_list(df_trending, config.OUTPUT_DIR_OTHERS, "TRENDING.csv")
        tools.save_list(df_gainers, config.OUTPUT_DIR_OTHERS, "GAINERS.csv")
        tools.save_list(df_loosers, config.OUTPUT_DIR_OTHERS, "LOOSERS.csv")
        tools.save_list(df_undervaluated, config.OUTPUT_DIR_OTHERS, "UNDERVALUATED.csv")

    if (config.GET_IBOVESPA == True):
        df_IBOVESPA = scrap_yahoo_list.get_list_IBOVESPA()
        tools.save_list(df_IBOVESPA, config.OUTPUT_DIR_OTHERS, "IBOVESPA.csv")

    if (config.GET_NIFTY == True):
        df_NIFTY = scrap_yahoo_list.get_list_NIFTY50()
        tools.save_list(df_NIFTY, config.OUTPUT_DIR_OTHERS, "NIFTY50.csv")
        df_NIFTY = scrap_yahoo_list.get_list_NIFTY_BANK()
        tools.save_list(df_NIFTY, config.OUTPUT_DIR_OTHERS, "NIFTYBANK.csv")