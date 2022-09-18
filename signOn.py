import streamlit as st
import webbrowser


# if 'password_correct' not in st.session_state:
#     st.session_state['username'] = st.secrets["passwords"]

def password_entered():
    """Checks whether a password entered by the user is correct."""
    if (
        st.session_state["username"] in st.secrets["passwords"]
        and st.session_state["password"]
        == st.secrets["passwords"][st.session_state["username"]]
    ):
        st.session_state["password_correct"] = True
        del st.session_state["password"]  # don't store username + password
        del st.session_state["username"]
    else:
        st.session_state["password_correct"] = False

def check_password():
    if "password_correct" not in st.session_state:
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False

    elif st.session_state["password_correct"]:
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("Error")
        return False

    else:
        st.write("Username and Password are registered. ")
        return True

if check_password():
    st.write("Here goes Hellosign API app...")
    st.write(st.session_state["password_correct"])


# Needs to check if user has non-registered username 