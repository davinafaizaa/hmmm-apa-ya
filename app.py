import streamlit as st

#Hirarki teks
st.title("📊 Dashboard")
st.header("Laporan Bulanan")
st.subheader("Monthly Expenses")
st.write(" with love using streamlit"
        )
title = st.text_input("Movie title", "Pride and Prejudice")
st.write("The current movie title is", title)
