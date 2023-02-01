#Importar bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo a base de dados
df_vendas = pd.read_excel("Vendas.xlsx")
df_produtos = pd.read_excel("Produtos.xlsx")
df = pd.merge(df_vendas,df_produtos, how="left", on="ID Produto")

# Novas colunas
df["custo"] = df["Custo Unitário"] * df["Quantidade"]
df["Lucro"] = df["Valor Venda"] - df["custo"]
df["mes_ano"] = df["Data Venda"].dt.to_period("M").astype(str)

# Agrupamentos




#dataApp
def main():
    st.title{"Análise de Vendas"}


if __name__ == "__main__":
    main()