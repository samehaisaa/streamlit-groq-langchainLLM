import streamlit as st
from chatbot import GroqChatbot

# Initialize chatbot instance
chatbot = GroqChatbot()

# Streamlit app
def main():
    st.title("Groq Chatbot 🤖")
    st.write("Hello! I'm your friendly Groq chatbot. Let's chat!")

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []  # Initialize chat history

    user_input = st.text_input("You:", placeholder="Type your message here...")

    if user_input:
        # Generate a response using the chatbot
        response = chatbot.get_response(user_input)
        # Save conversation history
        st.session_state["chat_history"].append({"user": user_input, "bot": response})

    # Display chat history
    if st.session_state["chat_history"]:
        for chat in st.session_state["chat_history"]:
            st.write(f"**Semah:** {chat['user']}")
            st.write(f"**dumb ugly bot:** {chat['bot']}")

if __name__ == "__main__":
    main()
