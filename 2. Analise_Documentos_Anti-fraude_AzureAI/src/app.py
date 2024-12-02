import os
import sys
import streamlit as st

from services.credit_card_service import analise_credit_card
from services.blob_service import upload_file_to_blob_storage

def configure_interface():
    st.title("Upload de Arquivos DIO - desafio 2 - Azure - AntifraudeDocs")
    uploaded_file = st.file_uploader("Faça o upload do arquivo", type=["png", "jpg", "jpeg", "pdf"])
    if uploaded_file is not None:
        filename = uploaded_file.name
        blob_url = upload_file_to_blob_storage(uploaded_file, filename)
        if blob_url:
            st.write(f"Arquivo {filename} enviado com sucesso para o Azure Blob Storage!")
            credit_card_info = analise_credit_card(blob_url)
            print(credit_card_info)
            try:
                if credit_card_info and credit_card_info['card_name']:
                    st.write(f"Cartão Analisado")
                else:
                    st.markdown(f"<h1 style='color:red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
                    st.write("Este não parece ser um cartão de crédito válido.")
            except Exception as e:
                st.write(f"Ocorreu um erro ao analisar o cartão: {str(e)}")
            show_image_and_validate(blob_url, credit_card_info)
        else:
            st.write(f"Falha ao enviar o arquivo {filename} para o Azure Blob Storage.")
def show_image_and_validate(blob_url, credit_card_info):
        st.image(blob_url, caption="Imagem carregada", use_container_width=True)
        st.write("Resultado da Validação:")
        try:
            if credit_card_info and credit_card_info['card_name']:
                st.markdown(f"<h1 style='color:green;'>Cartão Validado</h1>", unsafe_allow_html=True)
                st.write(f"Nome do Titular: {credit_card_info['card_name']}")
                st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
                st.write(f"Validade do Cartão: {credit_card_info['expiry_date']}")
            else:
                st.markdown(f"<h1 style='color:red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
                st.write("Este não parece ser um cartão de crédito válido.")
        except Exception as e:
            st.write(f"Ocorreu um erro ao validar o cartão: {str(e)}")
if __name__ == "__main__":
   configure_interface()