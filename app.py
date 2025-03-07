import streamlit as st
import random
import string
import openai  # Ensure you have OpenAI's library installed

# OpenAI API Key - Set your API Key Here
OPENAI_API_KEY = "my_key"
openai.api_key = OPENAI_API_KEY

def generate_password(length, use_special, use_numbers, use_ascii):
    characters = ""
    if use_ascii:
        characters += string.ascii_letters  # Uppercase and Lowercase letters
    if use_numbers:
        characters += string.digits  # Numbers 0-9
    if use_special:
        characters += string.punctuation  # Special Characters
    
    if not characters:
        return "Select at least one option!"
    
    return "".join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    length_score = len(password) / 2  # More length, better security
    diversity_score = len(set(password))  # Unique characters increase security
    strength = min(100, int((length_score + diversity_score) * 5))
    return strength

def chatbot_response(user_input):
    """Chatbot using OpenAI API"""
    if not user_input.strip():
        return "Please type something to chat."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit App UI
st.set_page_config(page_title="Password Generator & Chatbot", layout="wide")
st.sidebar.title("Options")

# Password Generator Section
st.title("🔐 Password Generator & Strength Meter")
password_length = st.sidebar.slider("Select Password Length", min_value=4, max_value=32, value=12)
use_special = st.sidebar.checkbox("Include Special Characters (@, #, $, etc.)")
use_numbers = st.sidebar.checkbox("Include Numbers (0-9)")
use_ascii = st.sidebar.checkbox("Include ASCII Letters (A-Z, a-z)", value=True)

if st.sidebar.button("Generate Password"):
    password = generate_password(password_length, use_special, use_numbers, use_ascii)
    strength = check_password_strength(password)
    
    st.success(f"Generated Password: `{password}`")
    st.progress(strength / 100)  # Show password strength visually
    st.write(f"**Password Strength: {strength}%**")

# Chatbot Section
st.sidebar.title("💬 Chatbot")
user_input = st.sidebar.text_input("Ask something:")
if st.sidebar.button("Chat"):
    response = chatbot_response(user_input)
    st.sidebar.write(response)
