import pandas as pd

result_df = employees_df[employees_df['mentor_id']!=3]['name'].to_frame().reset_index(drop=True)

print(result_df)