import sys
import pandas as pd
print('arguments',sys.argv)

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

month = int(sys.argv[1])
print(f'hello pipeline, month={month}')
df.to_parquet(f"output_day_{sys.argv[1]}.parquet")