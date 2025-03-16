from pyspark.sql import functions as F


result_df = categories_df.withColumn('cnt', F.size(F.split(F.col('products'), ', '))).select('category', 'cnt')

result_df.orderBy('cnt').show()