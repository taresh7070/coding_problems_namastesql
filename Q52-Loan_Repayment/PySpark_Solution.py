from pyspark.sql import functions as F

cte_df = payments_df.groupBy('loan_id').agg(
  											F.sum('amount_paid').alias('total_amount_paid'),
  											F.max('payment_date').alias('mx_payment_date')
											)

joined_df = loans_df.join(cte_df, on='loan_id')

joined_df = joined_df.withColumn('fully_paid_flag', 
                                 F.when(F.col('total_amount_paid')==F.col('loan_amount'), 1)
                                 .otherwise(0)
                                )

joined_df = joined_df.withColumn('on_time_flag', 
                                 F.when((F.col('total_amount_paid')==F.col('loan_amount')) & (F.col('due_date')>=F.col('mx_payment_date')), 1)
                                 .otherwise(0)
                                )

joined_df.select('loan_id', 'loan_amount', 'due_date', 'fully_paid_flag', 'on_time_flag').show()