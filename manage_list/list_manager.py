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
        if isinstance(df_actives, pd.DataFrame):
            df_actives.to_csv(config.OUTPUT_DIR_OTHERS+"ACTIVES.csv")
        if isinstance(df_trending, pd.DataFrame):
            df_trending.to_csv(config.OUTPUT_DIR_OTHERS+"TRENDING.csv")
        if isinstance(df_gainers, pd.DataFrame):
            df_gainers.to_csv(config.OUTPUT_DIR_OTHERS+"GAINERS.csv")
        if isinstance(df_loosers, pd.DataFrame):
            df_loosers.to_csv(config.OUTPUT_DIR_OTHERS+"LOOSERS.csv")
        if isinstance(df_undervaluated, pd.DataFrame):
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

def api_get_list(markets):
    result = {}

    if("euronext" in markets):
        df_EURONEXT = scrap_yahoo_list.get_list_EURONEXT()
        result["euronext"] = df_EURONEXT

    if("cac" in markets):
        df_CAC = scrap_wiki_list.get_list_CAC()
        result["cac"] = df_CAC

    if("dax" in markets):
        df_DAX = scrap_wiki_list.get_list_DAX()
        result["dax"] = df_DAX

    if("ftse" in markets):
        df_FTSE = scrap_yahoo_list.get_list_FTSE100()
        result["ftse100"] = df_FTSE
        df_FTSE = scrap_yahoo_list.get_list_FTSE250()
        result["ftse250"] = df_FTSE

    if ("nasdaq100" in markets):
        df_NASDAQ100 = scrap_wiki_list.get_list_NASDAQ100()
        result["nasdaq100"] = df_NASDAQ100

    if ("nasdaq" in markets):
        df_NASDAQ = scrap_yahoo_list.get_list_NASDAQ()
        result["nasdaq"] = df_NASDAQ

    if ("dji" in markets):
        df_DJI = scrap_wiki_list.get_list_DJI()
        result["dji"] = df_DJI
        df_DJI.to_csv(config.OUTPUT_DIR_US+"DJI.csv")
        df_DJI = scrap_yahoo_list.get_list_DOW()
        result["dow"] = df_DJI

    if ("sp500" in markets):
        df_SP500 = scrap_wiki_list.get_list_SP500()
        result["sp500"] = df_SP500
        df_SP500 = scrap_yahoo_list.get_list_yahoo_SP500()
        result["sp500_yahoo"] = df_SP500

    if ("yahoo" in markets):
        df_actives, df_trending, df_gainers, df_loosers, df_undervaluated = scrap_yahoo_list.get_list_YAHOO()
        if isinstance(df_actives, pd.DataFrame):
            result["actives"] = df_actives
        if isinstance(df_trending, pd.DataFrame):
            result["trending"] = df_trending
        if isinstance(df_gainers, pd.DataFrame):
            result["gainers"] = df_gainers
        if isinstance(df_loosers, pd.DataFrame):
            result["loosers"] = df_loosers
        if isinstance(df_undervaluated, pd.DataFrame):
            result["undervaluated"] = df_undervaluated

    if ("ibovespa" in markets):
        df_ibovespa = scrap_yahoo_list.get_list_IBOVESPA()
        result["ibovespa"] = df_ibovespa

    if ("nifty" in markets):
        df_NIFTY = scrap_yahoo_list.get_list_NIFTY50()
        if isinstance(df_NIFTY, pd.DataFrame):
            result["nifty50"] = df_NIFTY
        df_NIFTY = scrap_yahoo_list.get_list_NIFTY_BANK()
        if isinstance(df_NIFTY, pd.DataFrame):
            result["niftybank"] = df_NIFTY

    return result
