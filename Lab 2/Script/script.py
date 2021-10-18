import copy
import pandas as pd

df = pd.read_csv('../Data/tb.csv')
df.replace(float("NaN"), -1, inplace=True)
df_total = copy.copy(df)
df_total = pd.melt(df_total, id_vars=['iso2', 'year'], value_vars=['new_sp'],
                   var_name='column', value_name='disease')
df_total = df_total[df_total['disease'] != -1]
df_total['disease'] = df_total['disease'].astype(int)
df_total = df_total[['iso2', 'year', 'disease']]
df_total.to_csv('tb-total_disease.csv', index=False)
