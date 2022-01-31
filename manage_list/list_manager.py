import os
from init import config
from scraping import scrap_yahoo_list,scrap_wiki_list
import pandas as pd

def mk_directories():
    ALL_DIRS = [config.OUTPUT_DIR, config.OUTPUT_DIR_DATE, config.OUTPUT_DIR_MERGED,
        config.OUTPUT_DIR_RESULT, config.OUTPUT_DIR_MARKET, config.OUTPUT_DIR_EUROPE,
        config.OUTPUT_DIR_US, config.OUTPUT_DIR_ASIA, config.OUTPUT_DIR_OTHERS]
    for dir in ALL_DIRS:
        if not os.path.exists(dir):
            os.makedirs(dir)

def get_list():
    mk_directories()

    if(config.GET_EURONEXT == True):
        df_EURONEXT = scrap_yahoo_list.get_list_EURONEXT()
        df_EURONEXT.to_csv(config.OUTPUT_DIR_EUROPE+"EURONEXT.csv")

    if(config.GET_CAC == True):
        df_CAC = scrap_wiki_list.get_list_CAC()
        df_CAC.to_csv(config.OUTPUT_DIR_EUROPE+"CAC_40.csv")

    if(config.GET_DAX == True):
        df_DAX = scrap_wiki_list.get_list_DAX()
        df_DAX.to_csv(config.OUTPUT_DIR_EUROPE+"DAX.csv")

    if(config.GET_FTSE == True):
        df_FTSE = scrap_yahoo_list.get_list_FTSE100()
        df_FTSE.to_csv(config.OUTPUT_DIR_EUROPE+"FTSE100.csv")
        df_FTSE = scrap_yahoo_list.get_list_FTSE250()
        df_FTSE.to_csv(config.OUTPUT_DIR_EUROPE+"FTSE250.csv")

    if (config.GET_NASDAQ100 == True):
        df_NASDAQ100 = scrap_wiki_list.get_list_NASDAQ100()
        df_NASDAQ100.to_csv(config.OUTPUT_DIR_US+"NASDAQ100.csv")

    if (config.GET_NASDAQ == True):
        df_NASDAQ = scrap_yahoo_list.get_list_NASDAQ()
        df_NASDAQ.to_csv(config.OUTPUT_DIR_US+"NASDAQ.csv")

    if (config.GET_DJI == True):
        df_DJI = scrap_wiki_list.get_list_DJI()
        df_DJI.to_csv(config.OUTPUT_DIR_US+"DJI.csv")
        df_DJI = scrap_yahoo_list.get_list_DOW()
        df_DJI.to_csv(config.OUTPUT_DIR_US+"DOW.csv")

    if (config.GET_SP500 == True):
        df_SP500 = scrap_wiki_list.get_list_SP500()
        df_SP500.to_csv(config.OUTPUT_DIR_US+"SP500.csv")
        df_SP500 = scrap_yahoo_list.get_list_yahoo_SP500()
        df_SP500.to_csv(config.OUTPUT_DIR_US+"SP500_y.csv")

    if (config.GET_YAHOO == True):
        df_actives, df_trending, df_gainers, df_loosers, df_undervaluated = scrap_yahoo_list.get_list_YAHOO()
        if df_actives != None:
            df_actives.to_csv(config.OUTPUT_DIR_OTHERS+"ACTIVES.csv")
        if df_trending != None:
            df_trending.to_csv(config.OUTPUT_DIR_OTHERS+"TRENDING.csv")
        if df_gainers != None:
            df_gainers.to_csv(config.OUTPUT_DIR_OTHERS+"GAINERS.csv")
        if df_loosers != None:
            df_loosers.to_csv(config.OUTPUT_DIR_OTHERS+"LOOSERS.csv")
        if df_undervaluated != None:
            df_undervaluated.to_csv(config.OUTPUT_DIR_OTHERS+"UNDERVALUATED.csv")

    if (config.GET_IBOVESPA == True):
        df_IBOVESPA = scrap_yahoo_list.get_list_IBOVESPA()
        df_IBOVESPA.to_csv(config.OUTPUT_DIR_OTHERS+"IBOVESPA.csv")

    if (config.GET_NIFTY == True):
        df_NIFTY = scrap_yahoo_list.get_list_NIFTY50()
        if isinstance(df_NIFTY, pd.DataFrame):
            df_NIFTY.to_csv(config.OUTPUT_DIR_OTHERS+"NIFTY50.csv")
        df_NIFTY = scrap_yahoo_list.get_list_NIFTY_BANK()
        if isinstance(df_NIFTY, pd.DataFrame):
            df_NIFTY.to_csv(config.OUTPUT_DIR_OTHERS+"NIFTYBANK.csv")