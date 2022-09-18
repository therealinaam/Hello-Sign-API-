import streamlit as st
import webbrowser


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
    """Returns `True` if the user had a correct password."""

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        st.write("Do you need to sign in? ")
        if st.button("Sign in"):
            """"This has to be sign in page"""
            webbrowser.open('https://www.python.org') 
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("Here goes Hellosign API app...")
    st.button("Click me")
    st.write(st.session_state["password_correct"])
    