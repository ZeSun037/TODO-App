import streamlit as st
import functions

todos = functions.get_todos()

st.title("Your Todos...")
st.subheader("Manage your todos here to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo here.")
