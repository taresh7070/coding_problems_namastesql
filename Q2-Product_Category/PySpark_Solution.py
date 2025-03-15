from pyspark.sql import functions as F

from pyspark.sql.functions import when

products_df = products_df.withColumn('category', when(products_df.price<100, 'Low Price')
                                                 .when(((products_df.price>=100) & (products_df.price<=500)), 'Medium Price')
                                                 .otherwise('High Price'))


count_df = products_df.groupBy(['category']).agg(F.count('product_id').alias('cnt'))

#count_df.orderBy(F.desc('cnt')).show()

count_df.orderBy(F.col('cnt').desc()).show()