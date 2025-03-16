import pandas as pd

joined_df = products_df.merge(purchases_df[purchases_df['stars']>3], how='left', left_on='id', right_on='product_id')[['category', 'price', 'product_id']]

joined_df.loc[joined_df['product_id'].notna(), 'new_price'] = joined_df.price

result_df = joined_df.groupby(['category'], as_index=False).agg(price=('new_price', 'min'))

result_df['price'].fillna(0, inplace=True)

result_df['price']=result_df['price'].astype('Int64')

print(result_df)