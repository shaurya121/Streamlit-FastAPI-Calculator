import streamlit as st
import json
import requests

st.title('BASIC CALCULATOR APP')

# taking user inputs
option=st.selectbox("Select operation you want to perform?", ('+ Addition', '- Subtraction', '* Multiplication', '/ Division'))

st.write("")
st.write("Select the numbers using slider:")
x=st.slider("X", 0, 100, 20)
y=st.slider("Y", 0, 130, 10)

# converting inputs into json format
inputs={"operation": option, "x":x, "y":y}

# when the user clicks on button it will fetch API
if st.button('Calculate'):
	res=requests.post(url="http://127.0.0.1:8000/calculate", data=json.dumps(inputs))
	st.subheader(f"Response from API = {res.text}")

