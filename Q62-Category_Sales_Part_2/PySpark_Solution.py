from pyspark.sql import functions as F


joined_df = categories_df.join(sales_df, how='left', on='category_id')

result_df = joined_df.groupBy(F.col('category_name')).agg(F.sum(F.coalesce(F.col('amount'), F.lit(0))).alias('total_sales'))

result_df.orderBy('total_sales').show()