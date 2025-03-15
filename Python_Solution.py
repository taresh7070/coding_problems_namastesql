import pandas as pd

'''
print(orders_df)
print(returns_df)
'''

result_df = pd.merge(orders_df, returns_df, how='left', on='order_id')

count_df = result_df.groupby(result_df['customer_name'], as_index=False).agg(total_orders=('order_id', 'count'), return_total=('return_date', 'count'))

'''
count_df['return_prc']=((count_df['return_date'].values/count_df['order_date'].values)*100)

print(count_df[count_df['return_prc']>50][['customer_name', 'return_prc']])
'''
count_df['return_prc']=((count_df['return_total']/count_df['total_orders'])*100).round(2)

high_return_customers = count_df.loc[count_df['return_prc'] > 50, ['customer_name', 'return_prc']]

print(high_return_customers)