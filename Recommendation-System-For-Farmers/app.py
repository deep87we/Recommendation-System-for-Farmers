import streamlit as st
from model1 import show_model1
from model2 import show_model2
# Remove whitespace from the top of the page and sidebar
st.write('<style>div.block-container{padding-top:0.5rem;}</style>', unsafe_allow_html=True)
html_temp = """
    <div>
    <h1 style="color:Blue;text-align:center;">  Recommendation System for Farmers  </h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)
page=st.sidebar.selectbox("Crop Recommender or Fertilizer Recommender",("Crop","Fertilizer"))
if page=="Crop":
    show_model1()
else:
    show_model2()
