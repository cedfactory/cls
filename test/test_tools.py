import pytest
import pandas as pd

from manage_list import tools

class TestTools:

    def test_get_input_list(self):
        list_files = tools.get_input_list("./test/data/CSL_US.csv")
        assert (list_files == ['NASDAQ100.csv', 'NASDAQ.csv', 'DJI.csv', 'DOW.csv', 'SP500.csv', 'SP500_y.csv'])
