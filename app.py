import streamlit as st
import random

    

st.title("🏆GUESS THE NUMBER!!")
st.write("Try to guess the number between 1 and 100.")



if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0





user_input=st.number_input("enter the number",min_value=1,max_value=100,step=1)


if st.button("submit"):
    st.session_state.attempts+=1

    if user_input < st.session_state.number_to_guess:
        st.warning("The number is Too low")
    elif user_input > st.session_state.number_to_guess:
        st.warning("The number is Too high")
    elif user_input == st.session_state.number_to_guess:
        st.balloons()
        st.success(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
        st.session_state.number_to_guess=random.randint(1,100)
        st.session_state.attempts=0
    