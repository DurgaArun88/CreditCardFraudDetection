import streamlit as st
import pickle
import numpy as np

df=pickle.load(open('CreditCard.pkl','rb'))
dtc=pickle.load(open('dtc.pkl','rb'))

st.title("CREDIT CARD FRAUD DETECTION")
input_data = st.text_input('Enter the input data')
input_split_data = input_data.split('\t')

submit = st.button('Predict')

if submit:
  features = np.asarray(input_split_data, dtype=np.float64)
  prediction = dtc.predict(features.reshape(1,-1))

  if prediction[0]==0:
    st.write('Valid Transaction')
  else:
    st.write('Fraud Transaction')
