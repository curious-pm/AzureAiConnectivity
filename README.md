## Join the Community
[Join Curious PM Community](https://nas.io/curious-pm) to connect, share, and learn with others!

---
# Azure OpenAI Chat

This project provides an easy-to-use chat interface built with Streamlit and Azure OpenAI API. Users can ask questions, receive AI-powered responses in real-time, and adjust model settings to refine responses.

## What the Code Does
This project allows users to interact with an AI chatbot powered by Azure OpenAI's GPT model. The app lets users enter queries, receive instant responses, and fine-tune parameters such as randomness and response diversity to meet their needs.

### Features:
- **Real-time Chat:** Instantly interact with AI through a user-friendly interface.
- **Streaming Responses:** Responses are displayed dynamically as they are generated.
- **Adjustable Parameters:** Users can modify settings like `temperature`, `top_p`, `frequency_penalty`, and `presence_penalty` to change response behavior.
- **Chat History:** Messages are saved throughout the session.
- **Error Handling:** Provides helpful messages if something goes wrong.

---

## How to Use It (Step by Step)

### 1. Install Dependencies
Make sure Python is installed, then install the required libraries:

```bash
pip install -r requirements.txt
```

### 2. Set Up API Credentials
You will receive Azure OpenAI API credentials. Add them to a configuration file.

Create a `.streamlit/secrets.toml` file with the following content:

```toml
AZURE_OPENAI_API_ENDPOINT = "your-api-endpoint-here"
AZURE_OPENAI_API_KEY = "your-api-key-here"
```

### 3. Run the Application
Start the chatbot app with the command:

```bash
streamlit run app.py
```

### 4. Interact with the Chatbot
1. Type your query in the input field.
2. See responses appear in real-time.
3. Adjust AI settings from the sidebar.
4. Reset settings to default if needed.

### 5. Implementing at Your End
Follow these steps to build the chatbot on your own:

1. **Install the Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Write the Chatbot Code:**
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
   Store credentials safely in `.streamlit/secrets.toml`.

4. **Customize Your Chatbot:**
   Change the layout and parameters to match your needs.

5. **Run the Chatbot Locally:**
   ```bash
   streamlit run app.py
   ```

6. **Deploy the Chatbot:**
   Use platforms like Heroku, AWS, or Azure to make it available online.

---

## What Happens in Each Step

1. **App Setup:**
   - Loads API credentials from the secrets file.
   - Prepares chat history storage.

2. **User Input:**
   - Users type their questions in the input field.

3. **Processing the Query:**
   - The app sends the query to Azure OpenAI API.
   - The response is streamed back to the app.

4. **Displaying Response:**
   - The AI-generated response is shown in the chat window.

5. **Adjusting Parameters:**
   - Users can fine-tune settings to control response style and content.

6. **Session Management:**
   - The app remembers previous chats during the session.

---

## Folder Structure

```
project-folder/
│-- app.py                # Main chatbot application script
│-- requirements.txt      # Dependencies needed to run the app
│-- .streamlit/            
│   └── secrets.toml      # Stores API credentials
│-- README.md             # Documentation of the project
```

---

## Expected Output Example

**Input:** "Tell me about AI"

**Output:** "AI stands for Artificial Intelligence, which enables machines to mimic human intelligence."

---

## Common Issues & Troubleshooting

1. **Invalid API Key:**
   - Double-check credentials in `.streamlit/secrets.toml`.

2. **Missing Modules:**
   - Install required packages using `pip install -r requirements.txt`.

3. **App Not Running:**
   - Ensure the correct command is used: `streamlit run app.py`.

4. **Slow Responses:**
   - Try reducing `max_tokens` in the API request.

---

## Security Considerations

- **Do not share your API keys.**
- Use environment variables for secure deployment.
- Regularly change API keys for better security.

---

## Link to Hosted Version
[View Live App](#) *(Insert actual deployment link here)*

---

## Screenshots

1. **Chat Interface:**  
   <img src="https://private-user-images.githubusercontent.com/190357403/406335391-c845b8b1-79b7-41b7-ad77-54d5d3a616b3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzc3MDI5NDQsIm5iZiI6MTczNzcwMjY0NCwicGF0aCI6Ii8xOTAzNTc0MDMvNDA2MzM1MzkxLWM4NDViOGIxLTc5YjctNDFiNy1hZDc3LTU0ZDVkM2E2MTZiMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEyNFQwNzEwNDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04NmNmMDExOTFlZDkzZWI3MGEzN2YwMGI5YWQ4YWUyMGQ0ZGViNzE2NGU3OWY4ZmE2NjhhN2VjNmU1ZDY4YzNiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.fTnL4zw_2M9k5hOQIpr711TIL6r5dkX01s5zFWjQHYA" style="max-width: 500px; height: auto;" alt="Chat Interface">

2. **Sidebar for Parameters:**  
   <img src="https://private-user-images.githubusercontent.com/190357403/406335392-eee51350-192b-431a-9c34-9e55be963e00.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzc3MDMxNjIsIm5iZiI6MTczNzcwMjg2MiwicGF0aCI6Ii8xOTAzNTc0MDMvNDA2MzM1MzkyLWVlZTUxMzUwLTE5MmItNDMxYS05YzM0LTllNTViZTk2M2UwMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEyNFQwNzE0MjJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yMDdiODYzMzNhNzRiNGU5MmNjNjFlYzRmMThiNTU3ZjhkMWY4YTY4NTE4YTc0ZmE4YTZlM2Y4ZjEzNzgxZjk1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Bef62FpaEBOv3tDfw9D_aCfCdGR0It9z6IFmh2AywdI" style="max-width: 500px; height: auto;" alt="Sidebar Parameters">


---

## Video Overview
*A short video walkthrough will be provided explaining the app's features and usage.*

