import pandas as pd

joined_df = pd.merge(sales_df, products_df, on='product_id')[['product_name', 'price', 'quantity']]


joined_df['sales_amount'] = joined_df['price'] * joined_df['quantity']

joined_df = joined_df[['product_name', 'sales_amount']]

result_df = joined_df.groupby(['product_name'], as_index=False).agg(total_sales_amount=('sales_amount', 'sum'))

result_df.sort_values(by='product_name', inplace=True)

result_df.reset_index(drop=True, inplace=True)

print(result_df)