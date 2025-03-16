from pyspark.sql import functions as F

filter_df = sales_df.filter(
  							(F.month('order_date')==2)
                            & (F.year('order_date')==2022)
                            & (~F.dayofweek('order_date').isin([7, 1]))
                           )

result_df = filter_df.groupBy('category').agg(F.sum('amount').alias('total_sales')).orderBy('total_sales')

result_df.show()