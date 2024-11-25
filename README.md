# Academic Queries Assistant RAG

This is a simple chatbot application that integrates **Groq API** and **LangChain** to provide fast responses. The app uses Streamlit as a frontend for interaction with users.

## Table of Contents
1. [Installation](#installation)
2. [Generate API Key](#generate-api-key)
3. [Run the App](#run-the-app)
4. [License](#license)

## Installation

To run this application, you need Python 3.7+ and the required dependencies.

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/samehaisaa/streamlit-groq-langchainLLM.git
    ```

2. Navigate to the project directory:

    ```bash
    cd streamlit-groq-langchainLLM
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Generate API Key

To use the Groq API, you need to generate an API key.

1. Go to the [Groq Developer Portal](https://www.groq.com/).
2. Log in or create an account if you don't have one.
3. Navigate to the API section and generate a new API key.
4. Copy the generated API key.

## Setting Up the API Key

1. **Create a `.env` file** in the project root directory.

2. Add your API key to the `.env` file in the following format:

    ```
    GROQ_API_KEY=your_generated_api_key_here
    ```

> **Note:** Do not share your `.env` file or API key publicly.

Alternatively, you can set the `GROQ_API_KEY` environment variable directly on your local system.

## Run the App

1. Ensure that the dependencies are installed.
2. Start the Streamlit app by running:

    ```bash
    streamlit run app.py
    ```

This will start the app locally and you can open it in your browser to interact with the chatbot.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
