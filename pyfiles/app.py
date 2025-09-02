import streamlit as st
import pandas as pd
import time

st.title('ChatGPT-Bro.0')
st.header("Bataiye, Aapke liye kya kiya Jaaye?")
st.subheader('aapki seva mein sada tatpar')

st.write('This is a normal text')
st.markdown("""
###My Favorite movies
- Race3
- Humshakals
- Housefull
""")

st.code("""
def foo(input):
        return foo**2
        
x=foo(2)""")

st.latex('x^2 + y^2 + 2 = 0')

df = pd.DataFrame({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks':[50,60,70],
    'package':[10,12,14]
})

st.dataframe(df)

st.metric('Revenue', 'Rs 3L', '-3%')

st.json({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks':[50,60,70],
    'package':[10,12,14]
})

st.image('milleniumPark.jpg')

st.sidebar.dataframe(df)

col1, col2= st.columns(2)
with col1:
    st.image('milleniumPark.jpg')
with col2:
    st.text('Yeh Millenium park hai in Chicago')

st.error('Login Failed')
st.success('Login Ho gaya bhai')

st.color_picker('dark')

bar=st.progress(0)
for i in range(1,101):
    #time.sleep(.1)
    bar.progress(i)

Email = st.text_input('Enter Email')
number = st.number_input('Yaha sirf number jayega')
date = st.date_input('Yaha sirf Date hi jayegi')

st.balloons('Click here')