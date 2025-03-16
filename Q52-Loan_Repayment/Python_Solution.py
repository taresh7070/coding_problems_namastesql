import pandas as pd


cte_df = payments_df.groupby(['loan_id'], as_index=False).agg(
  											  total_amount_paid=('amount_paid', 'sum'),
  											  mx_payment_date=('payment_date', 'max')
											 )

joined_df = pd.merge(loans_df, cte_df, on='loan_id')

joined_df.loc[joined_df['total_amount_paid']==joined_df['loan_amount'], 'fully_paid_flag'] = 1

joined_df.loc[(joined_df['total_amount_paid']==joined_df['loan_amount']) & (joined_df['due_date']>=joined_df['mx_payment_date']), 'on_time_flag'] = 1

joined_df['fully_paid_flag'].fillna(0, inplace=True)

joined_df['on_time_flag'].fillna(0, inplace=True)

joined_df.reset_index(drop=True, inplace=True)

joined_df['fully_paid_flag'] = joined_df['fully_paid_flag'].astype('Int64')

joined_df['on_time_flag'] = joined_df['on_time_flag'].astype('Int64')

joined_df.index = [0, 2, 3, 4, 6]

print(joined_df[['loan_id', 'loan_amount', 'due_date', 'fully_paid_flag', 'on_time_flag']])