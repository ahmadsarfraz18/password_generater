import streamlit as st
import random
import string
import pandas as pd

# Function to generate password
def generate_password(length, use_numbers, use_special_chars, use_ascii_letters, exclude_similar):
    characters = ""
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    if use_ascii_letters:
        characters += string.ascii_letters
    
    if not characters:
        return "Please select at least one character type."
    
    # Exclude similar characters if enabled
    if exclude_similar:
        similar_chars = "1lI0O"
        characters = ''.join([char for char in characters if char not in similar_chars])
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to calculate password strength
def password_strength(password):
    strength = 0
    if len(password) >= 12:
        strength += 1
    if any(char in string.digits for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1
    if any(char in string.ascii_letters for char in password):
        strength += 1
    return strength

# Initialize session state for password history and theme
if 'password_history' not in st.session_state:
    st.session_state.password_history = []
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Streamlit UI
st.set_page_config(page_title="Password Generator", layout="wide")

# Dark Mode/Light Mode Toggle
if st.session_state.dark_mode:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #FFFFFF;
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

if st.sidebar.button("Toggle Dark Mode"):
    st.session_state.dark_mode = not st.session_state.dark_mode
    st.rerun()  # Use st.rerun() instead of st.experimental_rerun()

st.title("Secure Password Generator")

# Sidebar Options
st.sidebar.header("Customize Your Password")
password_length = st.sidebar.slider("Select Password Length", min_value=6, max_value=32, value=12)
use_numbers = st.sidebar.checkbox("Include Numbers")
use_special_chars = st.sidebar.checkbox("Include Special Characters")
use_ascii_letters = st.sidebar.checkbox("Include ASCII Letters", value=True)
exclude_similar = st.sidebar.checkbox("Exclude Similar Characters (e.g., 1, l, I, 0, O)")

# Generate Password Button
if st.sidebar.button("Generate Password"):
    password = generate_password(password_length, use_numbers, use_special_chars, use_ascii_letters, exclude_similar)
    st.session_state.password_history.append(password)
    st.success(f"Generated Password: `{password}`")
    
    # Copy to Clipboard
    if st.button("Copy to Clipboard"):
        st.write("Password copied to clipboard!")
        st.code(password)
    
    # Password Strength Indicator
    strength = password_strength(password)
    st.write("Password Strength:")
    if strength == 4:
        st.success("Strong 🔒")
    elif strength == 3:
        st.warning("Moderate 🔑")
    else:
        st.error("Weak 🔓")

# Password History
st.sidebar.header("Password History")
if st.session_state.password_history:
    for idx, pwd in enumerate(st.session_state.password_history, 1):
        st.sidebar.write(f"{idx}. `{pwd}`")
    
    # Export Passwords to CSV
    if st.sidebar.button("Export Passwords to CSV"):
        df = pd.DataFrame(st.session_state.password_history, columns=["Password"])
        df.to_csv("password_history.csv", index=False)
        st.sidebar.success("Passwords exported to `password_history.csv`")
else:
    st.sidebar.write("No passwords generated yet.")

# Footer
st.write("\n\n**Developed by Mahar Ahmad Sarfraz**")
