from pyspark.sql import functions as F


joined_df = products_df.join(purchases_df, how='left', on=((products_df.id==purchases_df.product_id) & (purchases_df.stars>3))).select('category', 'price', purchases_df.id)

result_df = joined_df.groupBy('category').agg(
  												F.coalesce(
                                                  F.min(F.when(F.col('id').isNotNull(), F.col('price'))), 
                                                  F.lit(0)
                                                ).alias('price')
											  )



result_df.orderBy('category').show()