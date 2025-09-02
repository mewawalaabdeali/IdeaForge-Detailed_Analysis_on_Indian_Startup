import streamlit as st
import pandas as pd

df = pd.read_csv('data/startup_funding.csv')

st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', sorted(df['Startup Name'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')
else:
    df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')
    st.sidebar.selectbox('Select Investor', sorted(df['Investors Name'].unique().tolist()))
    btn2 = st.siderbar.button('Find Investors Details')
    st.title('Investor Analysis')