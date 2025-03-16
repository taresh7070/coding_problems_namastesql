from pyspark.sql import functions as F

result_df = product_reviews_df.filter(~F.upper(F.col('review_text')).rlike('.*(NOT EXCELLENT|NOT AMAZING).*')
                                      & F.upper(F.col('review_text')).rlike('.*(EXCELLENT|AMAZING).*'))


result_df.show(truncate=False)