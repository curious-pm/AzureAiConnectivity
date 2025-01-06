# Azure OpenAI Chat

This is a simple web application built using Streamlit and the Azure OpenAI API that interacts with the GPT-4 model to generate responses based on user input.

## Overview

The application allows users to send queries to Azure OpenAI's GPT-4 model and receive responses in real-time. The app uses Streamlit for the frontend and Python for the backend, with requests made to the Azure API for AI-powered responses.

## How the App Was Built

The application uses **Streamlit** for the frontend to create an interactive chat interface. **Azure OpenAI API** is used for generating responses based on user queries. The app sends user input to the Azure OpenAI API and displays the generated response in the chat interface.## Code Structure

- **`app.py`**: This is the main Python script that contains the logic for the application. It handles:
  - User input and chat display using Streamlit components.
  - Sending requests to the Azure OpenAI API for generating responses.
  - Managing the chat history using `st.session_state`.

- **`.secrets.toml`**: This file stores sensitive credentials, such as your Azure OpenAI API endpoint and key, to keep them secure and out of the codebase.

- **`requirements.txt`**: A file that lists all the dependencies (Streamlit and Requests) required to run the app.


## Features
- **Chat Interface**: Users can type in a message and receive responses from GPT-4.
- **Session Management**: The application stores the chat history between the user and the assistant during the session.
- **Azure OpenAI Integration**: The app makes POST requests to the Azure OpenAI endpoint to generate AI responses.

## Prerequisites

To run this application locally, make sure you have the following installed:
- **Python** (version 3.7 or higher)
- **Streamlit**: A framework for building web applications
- **Requests**: A library to send HTTP requests

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

### Azure OpenAI API Key
To interact with the Azure OpenAI API, you will need to set up a secret with your API credentials. You can do this by:
1. Going to the Azure portal.
2. Creating an OpenAI resource and obtaining your **API endpoint** and **API key**.
3. Storing these credentials as secrets in your Streamlit app.

In your `.secrets.toml` file, add the following:

```bash
AZURE_OPENAI_API_ENDPOINT = "your_api_endpoint"
AZURE_OPENAI_API_KEY = "your_api_key"
```

## Running the Application

To run the application locally, follow these steps:
1. Clone or download the repository containing the app.
2. Set up your `secrets.toml` file with your Azure OpenAI API credentials.
3. Run the Streamlit app:

```bash
streamlit run app.py
```

This will open a web interface in your browser where you can start chatting with the AI.

## Code Structure

- **`app.py`**: This is the main Python script that contains the logic for the application. It handles:
  - User input and chat display using Streamlit components.
  - Sending requests to the Azure OpenAI API for generating responses.
  - Managing the chat history using `st.session_state`.

- **`.secrets.toml`**: This file stores sensitive credentials, such as your Azure OpenAI API endpoint and key, to keep them secure and out of the codebase.

- **`requirements.txt`**: A file that lists all the dependencies (Streamlit and Requests) required to run the app.


## How it Works

1. **User Input**: The user types a message into the chat input field.
2. **Request to API**: The application sends the user's message to the Azure OpenAI API.
3. **AI Response**: The API processes the message and sends a response back.
4. **Display Response**: The response is displayed in the chat interface, and the chat history is updated.
5. **Session Management**: The conversation history is maintained throughout the session using `st.session_state`.

## Troubleshooting

If you encounter issues:
- Make sure your **API credentials** are correct and that your Azure OpenAI resource is active.
- Check the terminal or Streamlit logs for any error messages.
- Ensure that all required Python packages are installed.
