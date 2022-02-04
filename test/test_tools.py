import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

from manage_list import tools

class TestTools:

    def test_get_input_list(self):
        list_files = tools.get_input_list("./test/data/CSL_US.csv")
        assert (list_files == ['NASDAQ100.csv', 'NASDAQ.csv', 'DJI.csv', 'DOW.csv', 'SP500.csv', 'SP500_y.csv'])

    def test_drop_df_duplicates(self):
        # context
        data_filename = "./test/data/test_drop_df_duplicates.csv"
        generated_filename = "./test/generated/test_drop_df_duplicates.csv"
        reference_filename = "./test/references/test_drop_df_duplicates.csv"
        df = pd.read_csv(data_filename)

        # action
        df = tools.drop_df_duplicates(df, "column1")

        # expectations
        df.to_csv(generated_filename)
        df_generated = pd.read_csv(generated_filename)
        df_reference = pd.read_csv(reference_filename)
        assert_frame_equal(df_generated, df_reference)

    def test_clean_up_df_symbol(self):
        # context
        data_filename = "./test/data/test_clean_up_df_symbol.csv"
        generated_filename = "./test/generated/test_clean_up_df_symbol.csv"
        reference_filename = "./test/references/test_clean_up_df_symbol.csv"

        # action
        tools.clean_up_df_symbol(data_filename, generated_filename)

        # expectations
        df_generated = pd.read_csv(generated_filename)
        df_reference = pd.read_csv(reference_filename)
        assert_frame_equal(df_generated, df_reference)
