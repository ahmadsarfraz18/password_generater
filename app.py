import streamlit as st
import random
import string

def generate_password(length, include_special, include_numbers, include_ascii):
    chars = ''
    if include_ascii:
        chars += string.ascii_letters
    if include_numbers:
        chars += string.digits
    if include_special:
        chars += string.punctuation
    
    if not chars:
        return "Please select at least one option!"
    
    return ''.join(random.choice(chars) for _ in range(length))

# Streamlit UI
st.set_page_config(page_title="Password Generator & Meter", layout="wide")
st.sidebar.title("Options")

# Sidebar options
length = st.sidebar.slider("Select Password Length", min_value=6, max_value=32, value=12)
include_special = st.sidebar.checkbox("Include Special Characters")
include_numbers = st.sidebar.checkbox("Include Numbers")
include_ascii = st.sidebar.checkbox("Include ASCII Letters", value=True)

if st.sidebar.button("Generate Password"):
    password = generate_password(length, include_special, include_numbers, include_ascii)
    st.write("### Generated Password:")
    st.code(password, language="")

# Simple Chatbot Functionality
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "generate password": "Go to the sidebar and click the generate button!",
        "bye": "Goodbye! Have a great day!"
    }
    return responses.get(user_input.lower(), "I'm not sure how to respond to that.")

st.sidebar.write("### Chatbot")
user_input = st.sidebar.text_input("Ask me something:")
if user_input:
    response = chatbot_response(user_input)
    st.sidebar.write(response)
