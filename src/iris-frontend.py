import streamlit as st
from PIL import Image
import requests

# header
image = Image.open("assets/header-iris.png")
st.image(image)
st.title("Iris Classifier App")
st.markdown('*easy way to predict leaves*')
st.divider()
st.subheader('Type the value then click Predict button.')

# form input
with st.form("iris-app-form"):
    sepal_length = st.number_input("Sepal Length", help="Type sepal length here. Value must be > 0.")
    sepal_width = st.number_input("Sepal Width", help="Type sepal width here. Value must be > 0.")
    petal_length = st.number_input("Petal Length", help="Type petal length here. Value must be > 0.")
    petal_width = st.number_input("Petal Width", help="Type petal width here. Value must be > 0.")

    # submit button
    submitted = st.form_submit_button("Predict")

    # check if button clicked
    if submitted:
        data = {
            "sepal_length":sepal_length,
            "sepal_width":sepal_width,
            "petal_length":petal_length,
            "petal_width":petal_width
        }

        # post request
        response = requests.post('http://backend:8000/predict', json=data)

        # get result
        result = response.json()

        # check response
        if result['code'] == 200:
            st.success(result['messages'])
            st.write(result['prediction'])
        else:
            st.error(result['messages'])