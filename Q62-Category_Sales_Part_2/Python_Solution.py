import pandas as pd

joined_df = pd.merge(categories_df, sales_df, how='left', on='category_id')

result_df = joined_df.groupby(['category_name'], as_index=False).agg(total_sales = ('amount', 'sum'))

result_df['total_sales'] = result_df['total_sales'].astype('Int64')

result_df.sort_values(by='total_sales', inplace=True)

result_df.reset_index(drop=True, inplace=True)

print(result_df)