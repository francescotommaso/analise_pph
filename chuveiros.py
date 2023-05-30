import pandas as pd


path = 'ANALISES/final.csv'

df = pd.read_csv(path, sep=';', on_bad_lines='skip')

print(df)



