import pandas as pd


filter_df = sales_df[
  					 (sales_df['order_date'].dt.month == 2)
  					 &(sales_df['order_date'].dt.year == 2022)
  					 &(~sales_df['order_date'].dt.dayofweek.isin([5, 6])) #Exclude Saturday (5) and Sunday (6) in Pandas
                    ]

result_df = filter_df.groupby(['category'], as_index=False).agg(total_sales = ('amount', 'sum'))

print(result_df)