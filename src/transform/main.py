#import bibliotecas
import pandas as pd
import sqlite3
from datetime import datetime

#carregar o dataframe 
df = pd.read_json('../../data/data.json', lines=True, dtype=False)
#print(df)

pd.options.display.max_columns = None #mostra todas as colunas no pandas

#origem da coleta e data e hora do processamento
df['sort'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
df['data_coleta'] = datetime.now()
#print(df)

df['old_price'] = df['old_price'].str.replace('.','').fillna(0).astype(int)
df['old_cent'] = df['old_cent'].fillna(0).astype(float)/100
df['new_price'] = df['new_price'].str.replace('.','').fillna(0).astype(int)
df['new_cent'] = df['new_cent'].fillna(0).astype(float)/100
df['rating'] = df['rating'].fillna(0).astype(float)
df['reviews'] = df['reviews'].str.replace('[\(\)]', '', regex=True)
df['reviews'] = df['reviews'].fillna(0).astype(int)

df['old'] = df['old_price'] + df['old_cent']
df['new'] = df['new_price'] + df['new_cent']

#print(df)

df = df.drop(columns=['old_price', 'old_cent', 'new_price', 'new_cent'])

#conetanto ao banco de dados
conn = sqlite3.connect('../../data/quotes.db')

df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

conn.close()

print(df)

df.to_csv("../../data/data_out.csv", index=False)