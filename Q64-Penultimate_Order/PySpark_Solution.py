from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Define partition by customer_name
window_spec = Window.partitionBy('customer_name').orderBy(F.col('order_date').desc())

cte_df = orders_df.withColumn('rw', F.rank().over(window_spec)) \
                  .withColumn('cnt', F.count('order_id').over(Window.partitionBy('customer_name')))

# Filter for second latest order OR customers with only one order
result_df = cte_df.filter((F.col('rw') == 2) | (F.col('cnt') == 1)) \
                  .select('order_id', 'order_date', 'customer_name', 'product_name', 'sales') \
                  .orderBy('customer_name')

result_df.show()
