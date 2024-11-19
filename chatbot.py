import os
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

# Set environment variables
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["TOKENIZERS_PARALLELISM"] = "false"  # To suppress HuggingFace warnings

class GroqChatbot:
    def __init__(self, model="llama3-8b-8192", memory_length=5):
        """
        Initialize the chatbot with model and memory settings.
        """
        groq_api_key = os.environ["GROQ_API_KEY"]
        self.groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name=model)
        self.memory = ConversationBufferWindowMemory(k=memory_length, memory_key="chat_history", return_messages=True)
        self.system_prompt = "You are a slay queen 2000s fashin icon conversational chatbot."

        # Construct the chat prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content=self.system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human_input}"),
        ])

        # Create the conversation chain
        self.conversation = LLMChain(
            llm=self.groq_chat,
            prompt=self.prompt,
            verbose=False,
            memory=self.memory,
        )

    def get_response(self, user_input):
        """
        Generates a response from the chatbot.
        """
        return self.conversation.predict(human_input=user_input)
