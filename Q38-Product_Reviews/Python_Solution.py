import pandas as pd

product_reviews_df['review_text'] = product_reviews_df['review_text'].str.upper()

result_df =  product_reviews_df[(~product_reviews_df['review_text'].str.contains('NOT EXCELLENT|NOT AMAZING', regex=True))
                                #& (~product_reviews_df['review_text'].str.contains('NOT AMAZING', regex=False))
                                & (product_reviews_df['review_text'].str.contains('AMAZING|EXCELLENT', regex=True))
                               ]

print(result_df)