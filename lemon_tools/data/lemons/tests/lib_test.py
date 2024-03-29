# -*- coding: utf-8 -*-

# import from standard library
import os
import proj
import pandas as pd
# import from your lib
from proj.lib import clean_data
import pytest

def test_clean_data():
    datapath = os.path.dirname(os.path.abspath(proj.__file__)) + '/data'
    df = pd.read_csv(f'{datapath}/data.csv.gz')
    first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
    assert list(df.columns)[:6] == first_cols
    assert df.shape == (999, 142)
    out = clean_data(df)
    assert out.shape == (985, 119)