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
    
    start = datetime.now()
    list_manager.get_list()
    end = datetime.now()
    out("\U0001F3C1 elapsed time : {}".format(end-start), step_format)

    input_file = str(sys.argv[2])
    merging_csv.merge_list(input_file + '.csv')
    if(config.FILL_DATA_FROM_DATABASE):
        fill_df_data.fill_df(input_file)
    else:
        # FILL DATA FROM YAHOO FINANCE
        scrap_profile.refresh_database(input_file)
