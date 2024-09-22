import pandas as pd

df = pd.read_csv(r"pokemon_data.csv")
df_xlsx = pd.read_excel("pokemon_data.xlsx")
# print(df.tail(3)) Use tail to check bottom roles, use head for top rows