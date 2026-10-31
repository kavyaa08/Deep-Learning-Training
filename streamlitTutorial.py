import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello,Streamlit")
st.write(":streamlit: This is your first streamlit app")
st.text("Lets get Started")

#conditional logic with widgets
name = st.text_input("Enter your name: ")
if st.button("Hello"):
    st.success(f"Hello,{name}!!")

# Displaying Data and Charts
df = pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

# File uploading and caching topics
upload_file = st.file_uploader("upload a csv",type='csv')
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.title(("Text and Markdown Demo"))
st.header("this is header")
st.subheader("this is subheader")
st.markdown("**Bold**,*Italic*,`Code`,[Link](https://streamlit.io)")
st.code("for i in range(5): print(i)", language="python")

st.text_input("what is your name")
st.text_area("write something..")
st.number_input("pick a number",min_value=0, max_value=99)
st.slider("Chooe a range",0,100)
st.selectbox("select a fruit",["Apple",'Banana','Mango'])
st.multiselect("Choose a topping",['Cheese','tomato'])
st.radio("Pick one",["Opt A","Opt B"])
st.checkbox("I agree to terms")


if st.checkbox("Show Details"):
    st.info("Here are more details...")

option = st.radio("choose view",["Show Chart","Show Table"])
if option == "Show Chart":
    st.write("Chart would apper here")
else:
    st.write("Table would apper here")


with st.form("login_form"):
    username=st.text_input("Username")
    password=st.text_input("Password",type="password")
    submitted=st.form_submit_button("Login")

    if submitted:
        st.success(f"Welcome,{username}!")

st.image("https://via.placeholder.com/300",caption="sample img",use_column_width=True)
st.video("https://www.youtube.com/watch?v=VqgUkExPvLY")


