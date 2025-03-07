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
    st.success(f"Generated Password: {password}")

# Footer
st.write("\n\n**Developed by Mahar Ahmad Sarfraz**")
