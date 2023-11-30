import streamlit as st
import random

def select_word():
    words = ["python", "hangman", "streamlit", "programming", "developer", "code"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def update_displayed_word(word, guessed_letters, displayed_word):
    match_found = False
    for i in range(len(word)):
        if word[i] in guessed_letters:
            displayed_word = displayed_word[:i] + word[i] + displayed_word[i+1:]
            match_found = True
    return displayed_word, match_found

def hangman():
    word_to_guess = st.session_state.get("word_to_guess", "")
    guessed_letters = st.session_state.get("guessed_letters", [])
    incorrect_guesses = st.session_state.get("incorrect_guesses", 0)
    max_incorrect_guesses = 6
    attempts_left = max_incorrect_guesses - incorrect_guesses

    st.title("Hangman Game")

    if not word_to_guess:
        word_to_guess = select_word()
        st.session_state.word_to_guess = word_to_guess
        st.session_state.guessed_letters = []
        st.session_state.incorrect_guesses = 0

    displayed_word = display_word(word_to_guess, guessed_letters)  # Initialize displayed_word

    user_input = st.text_input("Enter a letter:", key="user_input")
    if user_input:
        guessed_letter = user_input.lower()

        if guessed_letter.isalpha() and len(guessed_letter) == 1:
            if guessed_letter in guessed_letters:
                st.warning("You've already guessed that letter. Try again.")
            else:
                guessed_letters.append(guessed_letter)
                displayed_word, match_found = update_displayed_word(word_to_guess, guessed_letters, displayed_word)

                if guessed_letter not in word_to_guess:
                    st.session_state.incorrect_guesses += 1
                    attempts_left -= 1
                    st.warning("Incorrect guess!")
                elif match_found:
                    st.success("Match found!")

        else:
            st.warning("Please enter a valid single letter.")

    st.write("Updated Word:")
    st.text(displayed_word)

    st.write(f"Attempts left: {max(0, attempts_left)}")

    if "_" not in displayed_word:
        st.success("Congratulations! You guessed the word.")
        st.balloons()
        play_again_button = st.button("Play Again", key="play_again")
        if play_again_button:
            st.session_state.word_to_guess = ""
            st.session_state.guessed_letters = []
            st.session_state.incorrect_guesses = 0

    elif attempts_left <= 0:
        st.error(f"Sorry, you've run out of guesses. The word was '{word_to_guess}'.")
        play_again_button = st.button("Play Again", key="play_again")
        if play_again_button:
            st.session_state.word_to_guess = ""
            st.session_state.guessed_letters = []
            st.session_state.incorrect_guesses = 0

# Run the game
hangman()
