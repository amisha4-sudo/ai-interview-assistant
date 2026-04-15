import streamlit as st

st.title("AI Interview Assistant")

question = st.text_input("Enter Question")
answer = st.text_area("Your Answer")

if st.button("Submit"):
    st.write("Evaluation will appear here")
