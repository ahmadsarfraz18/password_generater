import streamlit as st
import random
import string

# --- APP TITLE ---
st.set_page_config(page_title="Password Generator & Strength Meter", layout="wide")
st.title("🔐 Password Generator & Strength Meter")

# --- PASSWORD GENERATION FUNCTION ---
def generate_password(length, use_special, use_numbers, use_letters):
    characters = ""
    if use_special:
        characters += string.punctuation  # Special characters like @, #, $
    if use_numbers:
        characters += string.digits  # Numbers 0-9
    if use_letters:
        characters += string.ascii_letters  # A-Z, a-z
    
    if not characters:
        return "Please select at least one option!"
    
    return "".join(random.choice(characters) for _ in range(length))

# --- SIDEBAR ---
st.sidebar.header("Chatbot 🤖")
st.sidebar.write("Yahan aap chatbot se baat kar sakte hain!")
user_input = st.sidebar.text_input("Aap ka sawal: ")
if user_input:
    st.sidebar.write("Chatbot ka jawab: Sorry, ye feature abhi under development hai!")

# --- PASSWORD SETTINGS ---
st.subheader("⚙️ Customize Your Password")
password_length = st.slider("Password Length", min_value=4, max_value=32, value=12)
use_special = st.checkbox("Include Special Characters (@, #, $)")
use_numbers = st.checkbox("Include Numbers (0-9)")
use_letters = st.checkbox("Include ASCII Letters (A-Z, a-z)", value=True)

if st.button("Generate Password"):
    password = generate_password(password_length, use_special, use_numbers, use_letters)
    st.success(f"Your Generated Password: `{password}`")
    
    # Password Strength Meter
    if len(password) < 8:
        st.error("Weak Password ❌")
    elif len(password) < 12:
        st.warning("Moderate Password ⚠️")
    else:
        st.success("Strong Password ✅")

# --- FOOTER ---
st.write("💡 Tip: Always use a strong password to secure your accounts!")
