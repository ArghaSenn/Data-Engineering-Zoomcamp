import sys
import pandas as pd

print('argument', sys.argv)
month = int(sys.argv[1])

df = pd.DataFrame({"day":[1, 2], "num_passengers":[3, 5]})
df['months'] = month
print(df)

df.to_parquet(f"output_{month}.parquet")

print(f'hello pipleline, month {month}')