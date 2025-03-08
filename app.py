# Import necessary libraries
import streamlit as st  # For creating the web app
import random  # For generating random characters
import string  # For accessing character sets (digits, punctuation, letters)
import pandas as pd  # For exporting password history to CSV

# Function to generate a password based on user preferences
def generate_password(length, use_numbers, use_special_chars, use_ascii_letters, exclude_similar):
    characters = ""  # Initialize an empty string to store allowed characters
    
    # Add numbers to the character set if the user selects this option
    if use_numbers:
        characters += string.digits  # Digits: 0-9
    
    # Add special characters to the character set if the user selects this option
    if use_special_chars:
        characters += string.punctuation  # Special characters: !@#$%^&*(), etc.
    
    # Add ASCII letters to the character set if the user selects this option
    if use_ascii_letters:
        characters += string.ascii_letters  # Letters: a-z, A-Z
    
    # If no character type is selected, return an error message
    if not characters:
        return "Please select at least one character type."
    
    # Exclude similar-looking characters if the user selects this option
    if exclude_similar:
        similar_chars = "1lI0O"  # Characters that look similar (e.g., 1, l, I, 0, O)
        characters = ''.join([char for char in characters if char not in similar_chars])
    
    # Generate the password by randomly selecting characters from the allowed set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to calculate the strength of a password
def password_strength(password):
    strength = 0  # Initialize strength score
    
    # Add 1 point if the password length is 12 or more
    if len(password) >= 12:
        strength += 1
    
    # Add 1 point if the password contains numbers
    if any(char in string.digits for char in password):
        strength += 1
    
    # Add 1 point if the password contains special characters
    if any(char in string.punctuation for char in password):
        strength += 1
    
    # Add 1 point if the password contains letters
    if any(char in string.ascii_letters for char in password):
        strength += 1
    
    return strength  # Return the total strength score (0-4)

# Initialize session state for password history and dark mode
if 'password_history' not in st.session_state:
    st.session_state.password_history = []  # Store generated passwords
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False  # Track dark mode state

# Streamlit UI Configuration
st.set_page_config(page_title="Password Generator", layout="wide")

# Dark Mode/Light Mode Toggle
if st.session_state.dark_mode:
    # Apply dark mode styles
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1E1E1E;  # Dark background
            color: #FFFFFF;  # White text
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    # Apply light mode styles
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #FFFFFF;  # Light background
            color: #000000;  # Black text
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Toggle Dark Mode Button
if st.sidebar.button("Toggle Dark Mode"):
    st.session_state.dark_mode = not st.session_state.dark_mode  # Switch between dark and light mode
    st.rerun()  # Rerun the app to apply the new theme

# App Title
st.title("Secure Password Generator")

# Sidebar Options for Customizing Password
st.sidebar.header("Customize Your Password")
password_length = st.sidebar.slider("Select Password Length", min_value=6, max_value=32, value=12)  # Password length slider
use_numbers = st.sidebar.checkbox("Include Numbers")  # Checkbox to include numbers
use_special_chars = st.sidebar.checkbox("Include Special Characters")  # Checkbox to include special characters
use_ascii_letters = st.sidebar.checkbox("Include ASCII Letters", value=True)  # Checkbox to include letters (enabled by default)
exclude_similar = st.sidebar.checkbox("Exclude Similar Characters (e.g., 1, l, I, 0, O)")  # Checkbox to exclude similar characters

# Generate Password Button
if st.sidebar.button("Generate Password"):
    # Generate a password based on user preferences
    password = generate_password(password_length, use_numbers, use_special_chars, use_ascii_letters, exclude_similar)
    st.session_state.password_history.append(password)  # Save the password to history
    st.success(f"Generated Password: `{password}`")  # Display the generated password
    
    # Copy to Clipboard Button
    if st.button("Copy to Clipboard"):
        st.write("Password copied to clipboard!")  # Confirmation message
        st.code(password)  # Display the password in a code block
    
    # Password Strength Indicator
    strength = password_strength(password)  # Calculate password strength
    st.write("Password Strength:")
    if strength == 4:
        st.success("Strong 🔒")  # Strong password
    elif strength == 3:
        st.warning("Moderate 🔑")  # Moderate password
    else:
        st.error("Weak 🔓")  # Weak password

# Password History Section
st.sidebar.header("Password History")
if st.session_state.password_history:
    # Display all saved passwords with an index
    for idx, pwd in enumerate(st.session_state.password_history, 1):
        st.sidebar.write(f"{idx}. `{pwd}`")
    
    # Export Passwords to CSV Button
    if st.sidebar.button("Export Passwords to CSV"):
        df = pd.DataFrame(st.session_state.password_history, columns=["Password"])  # Create a DataFrame
        df.to_csv("password_history.csv", index=False)  # Save to CSV
        st.sidebar.success("Passwords exported to `password_history.csv`")  # Confirmation message
    
    # Delete Password History Button
    if st.sidebar.button("Delete Password History"):
        st.session_state.password_history = []  # Clear the password history
        st.sidebar.success("Password history deleted!")  # Confirmation message
else:
    st.sidebar.write("No passwords generated yet.")  # Message if no passwords are generated

# Footer
st.write("\n\n**Developed by Mahar Ahmad Sarfraz**")  # Developer credit
