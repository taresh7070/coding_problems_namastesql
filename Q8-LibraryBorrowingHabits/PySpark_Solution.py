from pyspark.sql import functions as F


combine_df = borrowers_df.join(books_df, on='BookID')


result_df = combine_df.groupBy(['BorrowerName']).agg(F.concat_ws(",", F.sort_array(F.collect_list('BookName'))).alias('BorrowedBooks'))

result_df.orderBy('BorrowerName').show(truncate=False)