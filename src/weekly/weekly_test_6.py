from pathlib import Path
import pandas as pd
import statsmodels.api as sm

sp500 = pd.read_parquet('/Users/feketedalma/Documents/GitHub/ECOPY_23241/data/sp500.parquet', engine = 'fastparquet')

factors = pd.read_parquet('/Users/feketedalma/Documents/GitHub/ECOPY_23241/data/ff_factors.parquet', engine = 'fastparquet')

merged_df = pd.merge(sp500, factors, on='Date', how='left')

merged_df['Excess Return'] = merged_df['Monthly Returns'] - merged_df['RF']

merged_df = merged_df.sort_values(by='Date')
merged_df['ex_ret_1'] = merged_df.groupby('Symbol')['Excess Return'].shift(-1)

merged_df = merged_df.dropna(subset=['ex_ret_1'])
merged_df = merged_df.dropna(subset=['HML'])

amazon = merged_df[merged_df['Symbol'] == 'AMZN']
amazon = amazon.drop(columns=['Symbol'])

