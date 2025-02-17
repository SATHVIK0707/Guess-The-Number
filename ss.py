import streamlit as st
import random

# Initialize session state variables
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0

st.title("🎯 Guess the Number!")
st.write("Try to guess the number between 1 and 100.")

# User input for guessing
user_input = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if user_input < st.session_state.number_to_guess:
        st.warning("Too low! Try again.")
    elif user_input > st.session_state.number_to_guess:
        st.warning("Too high! Try again.")
    else:
        st.success(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
        st.session_state.number_to_guess = random.randint(1, 100)  # Reset the number
        st.session_state.attempts = 0  # Reset attempts