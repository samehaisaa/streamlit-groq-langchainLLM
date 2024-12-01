import streamlit as st
from chatbot import GroqChatbot

# Initialize chatbot instance
chatbot = GroqChatbot()

# Streamlit app
def main():
    st.set_page_config(page_title="Groq Chatbot", page_icon="🤖", layout="wide")  # Set page layout

    # Custom CSS for chat bubbles and styling
    st.markdown("""
        <style>
            .chat-container {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                padding: 20px;
            }
            .chat-bubble {
                padding: 10px 15px;
                border-radius: 20px;
                max-width: 80%;
                margin-bottom: 10px;
                background-color: #F1F1F1;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            .bot-bubble {
                background-color: #e0f7fa;
                align-self: flex-start;
            }
            .user-bubble {
                background-color: #c8e6c9;
                align-self: flex-end;
            }
            .chat-title {
                font-size: 2rem;
                font-weight: bold;
                color: #333;
                margin-bottom: 20px;
            }
            .chat-input {
                width: 100%;
                padding: 15px;
                margin-top: 20px;
                border-radius: 5px;
                border: 1px solid #ccc;
                font-size: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)

    # App title
    st.markdown("<h1 class='chat-title'>Groq Slaybot 🤖</h1>", unsafe_allow_html=True)
    st.write("Hello! I'm your friendly Groq chatbot. Let's chat!")

    # Initialize chat history in session state if not present
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # User input
    user_input = st.text_input("You:", placeholder="Type your message here...")

    if user_input:
        # Generate a response using the chatbot
        response = chatbot.get_response(user_input)
        
        # Save conversation history
        st.session_state["chat_history"].append({"user": user_input, "bot": response})

    # Display chat history with chat bubbles
    if st.session_state["chat_history"]:
        chat_container = st.container()
        with chat_container:
            for chat in st.session_state["chat_history"]:
                # Display user's message
                st.markdown(f'<div class="chat-bubble user-bubble">{chat["user"]}</div>', unsafe_allow_html=True)
                # Display bot's response
                st.markdown(f'<div class="chat-bubble bot-bubble">{chat["bot"]}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
