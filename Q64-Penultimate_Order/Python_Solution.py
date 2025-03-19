import pandas as pd

orders_df['rw'] = orders_df.groupby('customer_name')['order_date'].rank(method='first', ascending=False)
orders_df['cnt'] = orders_df.groupby('customer_name')['order_id'].transform('count')

filter_df = orders_df[(orders_df['rw']==2) | (orders_df['cnt']==1)]

result_df = filter_df[['order_id', 'order_date', 'customer_name', 'product_name', 'sales']].sort_values(by='customer_name').reset_index(drop=True)

print(result_df)