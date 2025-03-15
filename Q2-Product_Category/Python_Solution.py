import pandas as pd

import numpy as np


'''
products_df['category']= products_df['price'].case_when(
												[
                                                  (products_df['price']<100, 'Low Price'),
                                                  (((products_df['price']>=100) & (products_df['price']<=500)), 'Medium Price'),
                                                  (products_df['price']>500, 'High Price')
                                                ]
												)


products_df.loc[products_df.price<100, 'category']='Low Price'
products_df.loc[(products_df.price>=100) & (products_df['price']<=500), 'category']='Medium Price'
products_df.loc[products_df.price>500, 'category']='High Price'


products_df['category']=np.where(products_df['price']<100, 'Low Price',
                        np.where(((products_df['price']>=100) & (products_df['price']<=500)), 'Medium Price', 'High Price'))

'''

conditions = [
  products_df['price']<100,
  (products_df['price']>=100) & (products_df['price']<=500),
  products_df['price']>500
]

categories = ["Low Price", "Medium Price", "High Price"]

products_df['category']=np.select(conditions, categories, default='OutOfRange')

count_df = products_df.groupby(products_df['category'], as_index=False).agg(
count = ('product_id', 'count')
)

count_df.sort_values(by='count', inplace=True, ascending=False)
count_df.reset_index(drop = True, inplace = True)
print(count_df)