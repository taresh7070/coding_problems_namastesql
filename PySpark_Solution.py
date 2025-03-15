from pyspark.sql import functions as F
'''
orders_df.show()
returns_df.show()
'''

result_df = orders_df.join(returns_df, how='left', on='order_id')

count_df = result_df.groupBy(['customer_name']).agg(
  										F.count('order_id').alias('total_orders'),
										F.count('return_date').alias('return_total'))

count_df = count_df.withColumn(
  								'return_perc', 
  								F.round((F.col('return_total')/F.col('total_orders'))*100, 2)
)

high_return_cust = count_df.filter(F.col('return_perc')>50).select('customer_name', 'return_perc')

high_return_cust.orderBy(F.col('customer_name')).show()