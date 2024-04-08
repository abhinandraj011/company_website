import streamlit as st
import pandas


st.set_page_config(layout='wide')

st.header("The Best Company")
content= """A business description is most relevant 
when starting a company but is often effective when 
maintained regularly as a business grows. Depending on
the complexity of your business plan, it may be a brief 
paragraph or several pages long. When writing a business
description, it's important to consider your target audience.
Here are some intended audiences you might want to attract when 
creating an engaging description of your organization:"""
st.write(content)

st.subheader("Our Team")

col1,col2,col3=st.columns(3)
data=pandas.read_csv("../data.csv")
with col1:
    for index,row in data[:4].iterrows():
        temp= f"{row['first name']} {row['last name']}"
        st.subheader(temp.title())
        st.write(row['role'])
        st.image("images/"+row["image"])
with col2:
    for index,row in data[4:8].iterrows():
        temp = f"{row['first name']} {row['last name']}"
        st.subheader(temp.title())
        st.write(row['role'])
        st.image("images/" + row["image"])
with col3:
    for index,row in data[8:].iterrows():
        temp = f"{row['first name']} {row['last name']}"
        st.subheader(temp.title())
        st.write(row['role'])
        st.image("images/" + row["image"])




