import sys
import pandas as pd
import config

from tools import mk_directories
from tools import clean_up_df_symbol
from list_manager import get_list
from merging_csv import merge_list
from scrap_profile import get_info_list
from scrap_profile import refresh_database
from fill_df_data import fill_df
from scrap_isin import get_data_from_ISIN

sys.path.append("./compute_data/")
sys.path.append("./manage_list/")
sys.path.append("./merging/")
sys.path.append("./scraping/")
sys.path.append("./init/")

"""
    CSL module: Compute Symbol List
"""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    if (str(sys.argv[1]) == "--COLAB"):
        config.COLAB = True
    else:
        config.COLAB = False

    print(config.DATE)

    if(config.CLEAN_DATABASE == True):
        clean_up_df_symbol(config.INPUT_FILE_IMPORTED_DATA)
        clean_up_df_symbol(config.INPUT_FILE_IMPORTED_DATA_ISNI)

    mk_directories()

    get_list()

    input_file = str(sys.argv[2])
    input_file = input_file[2:]
    merge_list(input_file + '.csv')
    if(config.FILL_DATA_FROM_DATABASE):
        fill_df(input_file)
    else:
        # FILL DATA FROM YAHOO FINANCE
        refresh_database(input_file)


    print_hi('PyCharm')

