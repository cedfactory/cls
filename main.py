import sys
import pandas as pd
from init import config

from manage_list import tools,list_manager
from merging import merging_csv
from compute_data import fill_df_data
from scraping import scrap_profile
from datetime import datetime

sys.path.append("./compute_data/")
sys.path.append("./manage_list/")
sys.path.append("./merging/")
sys.path.append("./scraping/")
sys.path.append("./init/")

def _usage():
    print("--COLAB CSL_EUROPE")

step_format = "bold red"
def out(msg, format=None):
    if format:
        print("["+format+"]"+ msg + "[/"+format+"]")


"""
    CSL module: Compute Symbol List
"""
if __name__ == '__main__':

    if (str(sys.argv[1]) == "--COLAB"):
        config.COLAB = True
    else:
        config.COLAB = False

    print(config.DATE)

    if(config.CLEAN_DATABASE == True):
        tools.clean_up_df_symbol(config.INPUT_FILE_IMPORTED_DATA)
        tools.clean_up_df_symbol(config.INPUT_FILE_IMPORTED_DATA_ISNI)
    if(config.CLEAN_EURONEXT_DATABASE == True):
        tools.clean_up_df_symbol(config.INPUT_FILE_IMPORTED_DATA_EURONEXT)

    start = datetime.now()
    list_manager.get_list()
    end = datetime.now()
    out("\U0001F3C1 elapsed time : {}".format(end-start), step_format)

    input_file = str(sys.argv[2])
    merging_csv.merge_list(input_file + '.csv')
    if(config.FILL_DATA_FROM_DATABASE):
        symbol_list_filename_in = config.OUTPUT_DIR_RESULT + 'symbol_list_' + input_file + ".csv"
        symbol_list_filename_out = config.OUTPUT_DIR_RESULT + input_file + '_with_info' + ".csv"
        fill_df_data.fill_df(symbol_list_filename_in, symbol_list_filename_out)
    else:
        while True:
            # FILL DATABASE FROM YAHOO FINANCE
            print('RUN: ', config.REFRESH_DATABASE_LOOP)
            config.REFRESH_DATABASE_LOOP = config.REFRESH_DATABASE_LOOP + 1
            scrap_profile.refresh_database(input_file)

