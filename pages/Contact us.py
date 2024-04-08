import streamlit as st
import pandas
from send_email import send_email


st.header("Contact Us")
with st.form(key="email_forms"):
    user_email=st.text_input("Enter your Email Address")
    df=pandas.read_csv("topics.csv")


    option=st.selectbox("What topic do you want to discuss?",
                       df['topic'])
    raw_message=st.text_area("Text")
    message=f'''\
    Subject: New mail from [user_email]
    
    From: {user_email}
    Topic {option}
    {raw_message}
'''
    button=st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Mail sent Successfully")