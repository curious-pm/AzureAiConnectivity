# Azure OpenAI Chat

This project provides a simple chat interface using Streamlit and Azure OpenAI API to generate AI-powered responses in real-time. Users can interact with the chatbot and adjust model parameters for better control.

## What the Code Does
This project provides a Streamlit-based web application that allows users to interact with Azure OpenAI's GPT models in real-time. The app enables users to input queries and receive AI-generated responses via streaming. Additionally, it offers an intuitive sidebar for fine-tuning model parameters, ensuring better control over the chatbot's behavior.

### Features:
- **Real-time Chat:** Users can interact with the chatbot via a simple UI.
- **Streaming Responses:** AI-generated content appears dynamically as it is processed.
- **Customizable Parameters:** Users can adjust `temperature`, `top_p`, `frequency_penalty`, and `presence_penalty` to refine responses.
- **Session-based History:** Chat history is maintained throughout the session.
- **Error Handling:** Provides informative messages for API-related issues.

---

## How to Use It (Step by Step)

### 1. Install Dependencies
Ensure you have Python installed, then install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Set Up API Credentials
You will be provided with Azure OpenAI API credentials. Ensure you have the `API_ENDPOINT` and `API_KEY` ready.

Create a `.streamlit/secrets.toml` file in the root directory with the following content:

```toml
AZURE_OPENAI_API_ENDPOINT = "your-api-endpoint-here"
AZURE_OPENAI_API_KEY = "your-api-key-here"
```

### 3. Run the Application
Start the Streamlit app by executing the command:

```bash
streamlit run app.py
```

### 4. Interact with the Chatbot
1. Enter your query in the chat input field.
2. View responses streamed in real-time.
3. Adjust AI parameters from the sidebar.
4. Reset parameters to defaults if needed.

### 5. Implementing at Your End
To implement the same chatbot functionality from scratch, follow these steps:

1. **Set Up Environment:**
   - Install Python and required dependencies using:
     ```bash
     pip install -r req.txt
     ```

2. **Create Streamlit App:**
   - Create a new Python file, e.g., `app.py`, and write the following basic code:
     ```python
     import streamlit as st
     import requests

     st.title("Azure OpenAI Chat")

     endpoint = st.secrets["AZURE_OPENAI_API_ENDPOINT"]
     api_key = st.secrets["AZURE_OPENAI_API_KEY"]

     user_input = st.text_input("Enter your message")

     if st.button("Send"):
         response = requests.post(
             endpoint,
             headers={"api-key": api_key, "Content-Type": "application/json"},
             json={"messages": [{"role": "user", "content": user_input}], "max_tokens": 1000}
         )
         st.write(response.json())
     ```

3. **Secure API Credentials:**
   - Save your provided credentials securely in `.streamlit/secrets.toml`.

4. **Customize UI and Features:**
   - Modify the layout and parameters to enhance user experience.

5. **Run Your Application:**
   - Launch the app locally by running:
     ```bash
     streamlit run app.py
     ```

6. **Deploy the Application:**
   - Host your app on platforms like Heroku, AWS, or Azure App Services.

---

## Folder Structure

Here is an overview of the project structure to help you navigate:

```
project-folder/
│-- app.py                # Main Streamlit application script
│-- requirements.txt      # Dependencies required to run the app
│-- .streamlit/            
│   └── secrets.toml      # API credentials file
│-- README.md             # Documentation of the project
```

---

## Expected Output Example

When interacting with the chatbot, you should expect responses like the following:

**Input:** "Tell me about AI"

**Output:** "AI stands for Artificial Intelligence, which refers to the simulation of human intelligence in machines."

---

## Common Issues & Troubleshooting

1. **Invalid API Key Error:**
   - Ensure your API credentials are correctly added to `.streamlit/secrets.toml`.

2. **ModuleNotFoundError:**
   - Run `pip install -r req.txt` to install the required dependencies.

3. **Streamlit App Not Loading:**
   - Check if the correct port is open and the app is running using `streamlit run app.py`.

4. **Slow Response Time:**
   - Reduce `max_tokens` or adjust model parameters for better performance.

---

## Security Considerations

- **Never share your API keys publicly.**
- Use environment variables for storing sensitive data when deploying.
- Regularly rotate API keys to prevent unauthorized access.

---

## Link to Hosted Version
[View Live App](#) *(Insert actual deployment link here)*

---

## Join the Community
[Join Curious PM Community](https://nas.io/curious-pm) to connect, share, and learn with others!

---

## Screenshots

1. **Chat Interface:**
   ![Chat Screenshot](#) *(Insert screenshot link)*

2. **Sidebar for Parameters:**
   ![Sidebar Screenshot](#) *(Insert screenshot link)*

---

## Video Overview
*A short video walkthrough will be provided explaining the app's features and usage.*

