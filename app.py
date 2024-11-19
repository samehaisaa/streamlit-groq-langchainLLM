import streamlit as st

# Set page config and title
st.set_page_config(page_title="Groq Chatbot", page_icon=":robot_face:")

# Sidebar Instructions
st.sidebar.title("Groq Chatbot Instructions")
st.sidebar.write("""
Welcome to the Groq-powered chatbot! Ask me anything, and I'll respond quickly.
""")

# Display previous messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Custom HTML and CSS for bubbles and design
st.markdown("""
    <style>
    .user-message {
        background-color: #DCF8C6;
        border-radius: 20px;
        padding: 10px;
        margin: 10px 0;
        max-width: 75%;
        text-align: left;
    }
    .bot-message {
        background-color: #E5E5E5;
        border-radius: 20px;
        padding: 10px;
        margin: 10px 0;
        max-width: 75%;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

# Display messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">{message["content"]}</div>', unsafe_allow_html=True)

# User input
user_input = st.text_area("Ask a question:", height=100)

# Handle response and update chat
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Generating response..."):
        response = conversation.predict(human_input=user_input)
        st.session_state.messages.append({"role": "bot", "content": response})
        
    st.text_area("Ask a question:", "", key="input_field")
