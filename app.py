import streamlit as st
import random
import string

def generate_password(length, use_numbers, use_special_chars, use_ascii_letters):
    characters = ""
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    if use_ascii_letters:
        characters += string.ascii_letters
    
    if not characters:
        return "Please select at least one character type."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    """Calculate password strength based on length and character diversity."""
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

# Streamlit UI
st.set_page_config(page_title="Password Generator", layout="wide")
st.title("Secure Password Generator")

# Sidebar Options
st.sidebar.header("Customize Your Password")
password_length = st.sidebar.slider("Select Password Length", min_value=6, max_value=32, value=12)
use_numbers = st.sidebar.checkbox("Include Numbers")
use_special_chars = st.sidebar.checkbox("Include Special Characters")
use_ascii_letters = st.sidebar.checkbox("Include ASCII Letters", value=True)

# Generate Password Button
if st.sidebar.button("Generate Password"):
    password = generate_password(password_length, use_numbers, use_special_chars, use_ascii_letters)
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

# Footer
st.write("\n\n**Developed by Mahar Ahmad Sarfraz**")
