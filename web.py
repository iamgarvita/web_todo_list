import streamlit as st
import functions

todosss=functions.read_file()
def add_todo():
    todo=st.session_state["new_todo"]+"/n"
    todosss.append(todo)
    functions.write_files(todosss)


st.title("My To-Do App")
st.subheader("A man who cannot command himself will always live as a slave!")
st.write("This app is to command yourself so you can be productive")



for index, todo in enumerate(todosss):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todosss.pop(index)
        functions.write_files(todosss)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="What do you want to do? ", placeholder="Enter the task ", on_change=add_todo, key="new_todo")
