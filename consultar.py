import streamlit as st
import pandas as pd

import requests

st.set_page_config(page_title="Consulta de CEP", layout="centered")

st.title("📮 Consulte seu CEP")
st.write("Digite um CEP válido com 8 números e clique em **Buscar** para ver o endereço.")

cep = st.text_input("CEP:")
botao = st.button("🔍 Buscar")

def consultaCep(cep):
    url = "https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url.format(cep=cep))
    resposta.raise_for_status()
    return resposta.json()

if botao:
    if len(cep) == 8 and cep.isdigit():
        try:
            dados = consultaCep(cep)
            if "erro" in dados:
                st.error("CEP não encontrado")
            else:
                st.dataframe(pd.DataFrame([dados]), hide_index=True)
        except Exception as err:
            st.error("Erro na requisição. Verifique sua conexão.")
    else:
        st.warning("Digite um CEP válido com 8 dígitos numéricos.")
