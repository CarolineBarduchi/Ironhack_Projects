# entrar no cmd dentro da pasta em que esta o arquivo
# digitar o comando abaixo para abrir
# streamlit run calculadora.py 
import streamlit as st
import locale
import pandas as pd
import numpy as np
locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
df=pd.read_csv('secovi_bairros.csv')
df.rename(columns={'n_dormitorios':'N_DORMITORIOS', 'PRECO':'VALOR'}, inplace=True)

#############################

#Titulo
st.title('Calculadora de financiamento')

# primeira parte - media dos preços

#cria uma lista com os bairros
lista_bairros = df['BAIRROS'].unique()

#Usuario
input_bairro = st.selectbox('Escolha o bairro',lista_bairros)
input_dormitorios = st.selectbox('Quantidade de dormitórios',[1,2,3,4])
input_metragem = float(st.text_input('Qual a metragem?',100))

#Calcula o valor
valor = df[(df['BAIRROS'] == input_bairro) & (df['N_DORMITORIOS'] == input_dormitorios)].VALOR
preço = valor.values[0]*input_metragem
preço_print = locale.currency(preço,grouping=True,symbol=True)
st.write(f"Um apartamento com as característica que você procura custa em média {preço_print} reais.")


# Segunda parte - capital
montante = preço*0.2 # entrada de 20%
capital = float(st.text_input('Qual o capital atual?',100000))
aporte = float(st.text_input('Qual o aporte pretendido ao mês?',3000))
tempo = (np.nper(0.005, (aporte*(-1)), capital, montante))/12
financiamento = preço - montante
parcelas = np.pmt(0.07/12, 30*12, financiamento, fv=0)

parcelas_print = locale.currency(parcelas*-1, grouping=True, symbol=True)

apply_button = st.button("Tempo")

if apply_button:
    st.write(f"Serão necessários {round(tempo, 2)} anos para obter a entrada do seu apartamento.")
    st.write(f"Serão necessárias parcelas de R$ {parcelas_print} para o seu financiamento.")

