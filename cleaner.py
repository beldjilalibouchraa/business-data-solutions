import pandas as pd
print("CLEANER STARTING")

df = pd.read_csv('messy_sales.csv')
print("Data loaded:", len(df), "rows")

df['Name'] = df['Name'].str.title()
df['Region'] = df['Region'].str.upper()
df['Sales'] = df['Sales'].replace('[\$,]', '', regex=True).astype(int)

df.to_excel('cleaned.xlsx', index=False)
print("SAVED AS EXCEL FILE: cleaned.xlsx")
print("TOTAL SALES: $", df['Sales'].sum())