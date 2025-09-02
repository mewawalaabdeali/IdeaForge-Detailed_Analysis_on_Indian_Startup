import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.set_page_config(layout='wide', page_title='Startup ANalysis')
df = pd.read_csv('data/startup_cleaned.csv')

def load_investor_details(investor):
    st.title(investor_name)
    #load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor_name)].head()[['date', 'startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)

    with col1:
        #biggest_investments
        big_series = df[df['investors'].str.contains(investor_name)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig,ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')
else:
    #df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')
    investor_name=st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investors Details')
    if btn2:
        load_investor_details(investor_name)

    #st.title('Investor Analysis')