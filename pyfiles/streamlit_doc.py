import streamlit as st
import pandas as pd


email = st.text_input('Enter email')
password = st.text_input('Enter password',type='password')
gender = st.selectbox('Select gender',['male', 'Female'])

btn = st.button('Login Karo')

if btn:
    if email == 'Ali@gmail.com' and password=='1234':
        st.success('Login Ho gaya bhai!')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Fail ho giya')

file=st.file_uploader('Upload a CSV file')
if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())
    st.dataframe(df.head())