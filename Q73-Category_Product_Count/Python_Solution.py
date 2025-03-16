import pandas as pd

categories_df['cnt']=categories_df['products'].str.split(', ').apply(len)

result_df = categories_df[['category', 'cnt']]

result_df.sort_values(by='cnt', inplace=True)

result_df.reset_index(drop=True, inplace=True)

print(result_df)