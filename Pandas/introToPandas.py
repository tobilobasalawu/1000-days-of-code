import pandas as pd

#df = pd.read_csv(r"pokemon_data.csv")
#df_xlsx = pd.read_excel("pokemon_data.xlsx")
# print(df.tail(3)) Use tail to check bottom roles, use head for top rows

df = pd.read_csv("pokemon_data.txt", delimiter="\t")
#print(df)

#print(df.columns) #To print headers

#print(df[['Name', 'Type 1']]) #Printing out names
#print(df.iloc[1:4]) # index location

#for index,row in df.iterrows():
#    print(index,row['Name'])

#print(df.loc[df['Type 1'] == 'Fire'])
print(df.describe())