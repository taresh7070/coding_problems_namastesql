import pandas as pd


combine_df = pd.merge(borrowers_df, books_df, on='BookID')

combine_df = combine_df.groupby(['BorrowerName'], as_index=False).agg(BorrowedBooks=('BookName', lambda x : ",".join(sorted(x))))

print(combine_df.sort_values(by='BorrowerName'))