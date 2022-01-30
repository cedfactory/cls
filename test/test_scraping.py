import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

from scraping import scrap_yahoo_list

class TestScraping:

    def test_get_list_nasdaq(self):
        # action
        df = scrap_yahoo_list.get_list_NASDAQ()

        # expectations
        df.to_csv("./test/generated/list_nasdaq.csv")
        df_generated = pd.read_csv("./test/generated/list_nasdaq.csv")
        df_ref = pd.read_csv("./test/references/list_nasdaq.csv")
        assert_frame_equal(df_generated, df_ref)

    def test_get_list_yahoo_SP500(self):
        # action
        df = scrap_yahoo_list.get_list_yahoo_SP500()

        # expectations
        df.to_csv("./test/generated/list_sp500.csv")
        df_generated = pd.read_csv("./test/generated/list_sp500.csv")
        df_ref = pd.read_csv("./test/references/list_sp500.csv")
        assert_frame_equal(df_generated, df_ref)

    def test_get_list_dow(self):
        # action
        df = scrap_yahoo_list.get_list_DOW()

        # expectations
        df.to_csv("./test/generated/list_dow.csv")
        df_generated = pd.read_csv("./test/generated/list_dow.csv")
        df_ref = pd.read_csv("./test/references/list_dow.csv")
        assert_frame_equal(df_generated, df_ref)
       


