import pandas as pd


products_df = products_df.sort_values(by=['product_id', 'price_date'])

products_df['end_date'] = products_df.groupby('product_id')['price_date'].shift(-1)

products_df['end_date'] = products_df['end_date'].fillna('2028-12-31')

products_df['end_date'] = pd.to_datetime(products_df['end_date'])


joined_df = pd.merge(orders_df, products_df, on='product_id')

result_df = joined_df[
  					  (joined_df['order_date']>=joined_df['price_date'])
  					  &(joined_df['order_date']<joined_df['end_date'])
					 ][['product_id', 'price']]


result_df = result_df.groupby(['product_id'], as_index=False).agg(total_sales=('price', 'sum'))

print(result_df)