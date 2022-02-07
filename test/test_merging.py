import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

from merging import merging_csv

class TestMerging:

    def check_expectations(self, df, csvfile):
        assert(isinstance(df, pd.DataFrame))
        df.to_csv("./test/generated/"+csvfile)
        df_generated = pd.read_csv("./test/generated/"+csvfile)
        df_ref = pd.read_csv("./test/references/"+csvfile)
        assert_frame_equal(df_generated, df_ref)

    #
    # merge_list
    #

    def test_merge_list(self):
        pass
        df = merging_csv.merge_list("CSL_EURONEXT.csv", "./test/generated/test_merge_list.csv")
        self.check_expectations(df, "test_merge_list.csv")
