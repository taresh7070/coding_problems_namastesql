from pyspark.sql import functions as F
from pyspark.sql.window import Window

window_spec = Window.partitionBy('product_id').orderBy('price_date')

price_df = products_df.withColumn('end_date', F.coalesce(F.lead('price_date').over(window_spec), F.lit('9999-12-31')))

joined_df = orders_df.join(price_df, on='product_id')

joined_df = joined_df.filter(
  							 (F.col('order_date')>=F.col('price_date'))
  							 & (F.col('order_date')<F.col('end_date'))
							 ).select('product_id', 'price')

result_df = joined_df.groupBy('product_id').agg(F.sum('price').alias('total_sales'))

result_df.orderBy('product_id').show()