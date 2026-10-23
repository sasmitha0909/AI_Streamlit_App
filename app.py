import streamlit as st
st.title("AI-enabled Web Application")
st.write("You successfully deployed AI-enabled Web application using AWS EC2.")
32
name = st.text_input("Enter your name")
if st.button("Submit"):
  st.success(f"Hello, {name}! Your application is running successfully.")
