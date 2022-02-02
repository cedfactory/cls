import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

from compute_data import fill_df_data

class TestComputeData:

    def test_get_list_nasdaq(self):
        symbol_list_generated = "./test/generated/test_fill_df_data_symbol_list_CSL_EUROPE.csv"
        symbol_list_reference = "./test/references/test_fill_df_data_symbol_list_CSL_EUROPE.csv"
        symbol_list_isni_generated = "./test/generated/test_fill_df_data_symbol_list_isni_CSL_EUROPE.csv"
        symbol_list_isni_reference = "./test/references/test_fill_df_data_symbol_list_isni_CSL_EUROPE.csv"
        fill_df_data.fill_df("./test/data/test_fill_df_data_symbol_list_CSL_EUROPE.csv",
                                symbol_list_isni_generated,
                                symbol_list_generated)

        df_generated = pd.read_csv(symbol_list_generated)
        df_ref = pd.read_csv(symbol_list_reference)
        assert_frame_equal(df_generated, df_ref)

        df_generated = pd.read_csv(symbol_list_isni_generated)
        df_ref = pd.read_csv(symbol_list_isni_reference)
        assert_frame_equal(df_generated, df_ref)