from pyspark.sql import functions as F


joined_df = employees_df.join(departments_df, on='department_id')


result_df = joined_df.groupBy(F.col('department_name')).agg(
															F.round(F.avg('salary'), 2).alias('average_salary'),
  															F.count('employee_id').alias('cnt')
)
result_df = result_df.filter(F.col('cnt')>2)

result_df.orderBy(F.col('average_salary').desc()).select('department_name', 'average_salary').show()