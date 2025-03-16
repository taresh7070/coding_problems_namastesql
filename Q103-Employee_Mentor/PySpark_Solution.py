from pyspark.sql import functions as F

'''
filter_df = employees_df.filter(~(F.coalesce(F.col('mentor_id'), F.lit(0))==3)).select('name')

filter_df.show(truncate=False)
'''

employees_df.filter(~(F.coalesce(F.col('mentor_id'), F.lit(0))==3)).select('name').show(truncate=False)