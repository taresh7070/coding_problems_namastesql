import pandas as pd


joined_df = pd.merge(employees_df, departments_df, on='department_id')


result_df = joined_df.groupby(['department_name'], as_index=False).agg(
																		average_salary = ('salary', 'mean'),
  																		cnt = ('employee_id', 'count')
)

result_df = result_df[result_df['cnt']>2][['department_name', 'average_salary']]

result_df.sort_values(by = 'average_salary', ascending=False, inplace=True)

result_df.reset_index(drop=True, inplace=True)

print(result_df)