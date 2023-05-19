import streamlit as st
from Analysis import RFC, data
st.set_page_config(
    page_title="Crop Recommended",
    page_icon="🤖",
)

st.title(":green[Crop Recommendor]")
st.markdown("<p style = 'border : 1px solid; padding : 3px; align-text : center;' ><strong style=' text-color = red ';>Note :</strong> Please select the attribute values from sidebar</p>",unsafe_allow_html=True)

st.sidebar.header("Enter values here.")

N = st.sidebar.number_input("Nitrogen",min_value=0.0,step=10.0)
P = st.sidebar.number_input("Potassium",0.0,step=10.0)
K = st.sidebar.number_input("Sodium",min_value=0.0,step=10.0)
temperature = st.sidebar.number_input("Temperature *C",min_value=0.0,max_value=50.0,step=10.0)
humidity = st.sidebar.number_input("Humidity %",min_value=0.0,max_value=100.0,step=10.0)
ph = st.sidebar.number_input("PH",min_value=0.00,max_value=14.0,step=10.0)
rainfall = st.sidebar.number_input("Rainfall (CM)",min_value=0.0,max_value = 100.0,step=10.0)

if st.sidebar.button("Predict"):
    p = str(RFC.predict([[N,P,K,temperature,humidity,ph,rainfall]])[0])
    p = p.title()
    st.success(f"The recommended crop is: ")
    st.markdown(f"<h1 style = 'text-align : center; border : 3px solid red' ;>{p}</h1>",unsafe_allow_html=True)
