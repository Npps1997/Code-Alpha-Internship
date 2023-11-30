import streamlit as st
from nltk.chat.util import Chat, reflections
from datetime import datetime

# Patterns
patterns = [
    (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I\'m fine, how about you?']),
    (r'what is your name?', ['I am a chatbot. You can call me ChatGPT.', 'I don\'t have a name, but you can call me Chatbot.']),
    (r'quit|exit', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'what day is it\?', ['Today is {:%A, %B %d, %Y}.'.format(datetime.now())]),
    (r'what time is it\?', ['The current time is {:%H:%M}.'.format(datetime.now())]),
    (r'how old are you?', ['I don\'t have an age. I exist in the realm of code!']),
    (r'i love you', ['Thank you! I appreciate your kind words.']),
    (r'tell me a joke', ['Why don\'t scientists trust atoms? Because they make up everything!']),
    (r'favorite color', ['I don\'t have a favorite color. What\'s yours?']),
    (r'your creator', ['I was created by OpenAI.']),
    (r'thank you', ['You\'re welcome!', 'Anytime!', 'No problem.']),
    (r'sorry', ['No need to apologize. It\'s all good.']),
    (r'(.*)\?', ['I\'m not sure, could you please elaborate?', 'I\'m not an expert on that.']),
    (r'(.*)', ['Interesting. Tell me more.', 'I see. Please go on.', 'That\'s intriguing.']),
]

# chatbot instance
chatbot = Chat(patterns, reflections)

# initialize chat history
def get_chat_history():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    return st.session_state.chat_history

# Streamlit UI
def main():
    st.title("Chatbot with Streamlit")

    # conversation history
    conversation_history = st.empty()
    previous_chats = get_chat_history()
    for entry in previous_chats:
        conversation_history.text(
            f"{entry['timestamp']} - You: {entry['user_input']}\nChatbot: {entry['chatbot_response']}\n"
        )

    # User input
    user_input = st.text_input("You:", key="user_input")

    try:
        if st.button("Send"):
            if user_input.lower() in ['quit', 'exit']:
                st.text("Chatbot: Goodbye!")
            else:
                response = chatbot.respond(user_input)

                # Saving the conversation to the list
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                previous_chats.append({'timestamp': timestamp, 'user_input': user_input, 'chatbot_response': response})

                # Updating conversation history
                conversation_history.text(f"{timestamp} - You: {user_input}\nChatbot: {response}\n")

    except Exception as e:
        st.text(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
