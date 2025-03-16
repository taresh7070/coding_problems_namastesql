from pyspark.sql import functions as F

joined_df = sales_df.join(products_df, on='product_id')

result_df = joined_df.groupBy(F.col('product_name')).agg(F.sum(F.col('quantity')*F.col('price')).alias('total_sales_amount'))

result_df.orderBy('product_name').show(truncate=False)
