import streamlit as st
from PIL import Image

st.title("サンプルアプリ")
st.caption('これはテストアプリです')

image = Image.open('./data/chibi_2023122224742.png')
st.image(image, width=200)
