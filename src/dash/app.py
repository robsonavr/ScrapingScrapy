import streamlit as st
import pandas as pd
import sqlite3

#conecta ao banco de dados
conn = sqlite3.connect('../data/quotes.db')

#carrega os dados no dataframe
df = pd.read_sql_query("Select * From mercadolivre_items", conn)

#fecha a conexao
conn.close()

#titulo
st.title('Pesquisa de mercado - tenis corrida masculino')

#subtitulo
st.subheader('Principais KPIs')

#layout das colunas
st.write(df)
col1, col2, col3 = st.columns(3)

#KPI 1 numero total de itens
total_items = df.shape[0]
col1.metric(label='Número total de itens', value=total_items)

#KPI 2 quantidade de marcas disponiveis
qty_brands = df['brand'].nunique()
col2.metric(label='Quantidade de marcas', value=qty_brands)

#KPI 3 preco medio
average_price = df['new'].mean()
col3.metric(label='Preço médio (R$)', value=f'{average_price:.2f}')

#As marcas mais encontradas
st.subheader("As marcas mais encontradas")
col1, col2 = st.columns([4,2])
top10_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top10_brands[:10])
col2.write(top10_brands[:10])


#media por marca
st.subheader("Media por marca")
col1, col2 = st.columns([4,2])
mean_brands = df.groupby('brand')['new'].mean().sort_values(ascending=False)
col1.bar_chart(mean_brands[:10])
col2.write(mean_brands[:10])

#satisfacao por marca
st.subheader("Satisfação por marca")
col1, col2 = st.columns([4,2])
non_zero = df.loc[df['rating']>0]
satisfaction = non_zero.groupby('brand')['rating'].mean()
col1.bar_chart(satisfaction[:10])
col2.write(satisfaction[:10])