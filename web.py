import streamlit as st
import functions

todos = functions.get_todos()


def add_todos():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("Your Todos...")
st.subheader("Manage your todos here to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a todo here.",
              on_change=add_todos, key="new_todo")
