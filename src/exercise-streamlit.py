import streamlit as st
from PIL import Image

st.header('Predicting Leaf Shape, *in instant*')
st.subheader('Better learn, my boy!')
st.title('My first app!!')
st.markdown('wow!')
st.markdown('**hi**')
st.markdown('*check*')

image = Image.open('../assets/header-iris.png')
st.image(image, caption='bunch of rocks')


