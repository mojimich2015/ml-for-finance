#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from copy import copy
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

# READ THE STOCK CSV & SORT IT
stocks_df = pd.read_csv('stocks.csv')
stocks_df = stocks_df.sort_values(by = ['Date']) 

print("\n")
print('- Total Number Of Stocks: {}'.format(len(stocks_df.columns[1:])))
print('\n')

print("- List Of Stock Names:")
for i in stocks_df.columns[1:]:
    print("\t" + i)
print('\n')


# THE AVERAGE RETURN OF S&P500
stocks_df['sp500'].mean()

print("- STOCK THAT HAS THE MINIMUM DISPERTION OF MEAN : ")
print("\t" + 
      str(      stocks_df.std()[
          stocks_df.std().index.where(stocks_df.std().values == min(stocks_df.std())).notnull()
          ]) 
)

