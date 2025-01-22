## OpenAI 
The OpenAI Playground is a Streamlit-based web application that allows users to interact with Azure OpenAI models via a chat interface with real-time streaming responses.

## Detailed Explanation

This application provides a simple interface for users to enter prompts and receive responses from the Azure OpenAI API. It offers configurable parameters for fine-tuning the model's behavior and supports session-based chat history.

### Key Features:

- Real-time streaming responses from Azure OpenAI.
- Adjustable model parameters such as temperature, top\_p, frequency penalty, and presence penalty.
- Interactive chat UI with stored conversation history.
- Sidebar controls to adjust model behavior dynamically.
- Error handling and graceful degradation.

### Code Breakdown:

#### 1. `AzureOpenAIChat` Class

This class is responsible for:

- Retrieving API credentials securely from Streamlit secrets.
- Sending a POST request to the Azure OpenAI API endpoint.
- Handling streaming responses and parsing output tokens in real time.

#### 2. `main()` Function

The main function orchestrates the UI components and handles the following:

- Page configuration and title setup.
- Sidebar controls for adjusting model parameters.
- Chat input handling with real-time response streaming.
- Maintaining session-based chat history.

#### 3. Sidebar Controls

The sidebar allows users to adjust:

- `Temperature:` Controls randomness of responses.
- `Top P:` Limits token probability (nucleus sampling).
- `Frequency Penalty:` Reduces repetition of tokens.
- `Presence Penalty:` Encourages diverse topic generation.
- A reset button to restore default values.

#### 4. Chat Display

The conversation history is displayed using Streamlit's `st.chat_message()` function to alternate between user and assistant messages.

#### 5. Footer

A custom HTML footer provides credits with a link to the Curious-PM page.

## Installation Instructions

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone [repository-link]
   cd openai-playground
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your Azure OpenAI credentials to Streamlit secrets:
   ```plaintext
   AZURE_OPENAI_API_ENDPOINT = "your-api-endpoint"
   AZURE_OPENAI_API_KEY = "your-api-key"
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage Guidelines

1. Launch the application using the command `streamlit run app.py`.
2. Enter prompts in the chat input field.
3. Adjust the model parameters from the sidebar.
4. View AI-generated responses in real time.
5. Use the "Reset to Defaults" button to revert to original parameter settings.

## Code Walkthrough

The project structure is as follows:

```
openai-playground/
│-- app.py  # Main Streamlit application
│-- requirements.txt  # Dependencies
│-- .streamlit/secrets.toml  # API credentials
```

### Explanation of Files:

- **app.py**

  - The main entry point for the application.
  - *Initializes Streamlit UI, handles user interactions, and manages API* communication.
  - Example snippet:
    ```python
    st.set_page_config(page_title="OpenAI Playground", page_icon="💬")
    st.title("OpenAI Playground")
    ```
  - Handles chat input and responses via the `AzureOpenAIChat` class.

- **requirements.txt**

  - Lists the dependencies required to run the application.
  - Example snippet:
    ```plaintext
    streamlit
    requests
    ```
  - Install dependencies using `pip install -r requirements.txt`.

- **.streamlit/secrets.toml**

  - Stores API credentials securely.
  - Example snippet:
    ```plaintext
    AZURE_OPENAI_API_ENDPOINT = "your-api-endpoint"
    AZURE_OPENAI_API_KEY = "your-api-key"
    ```

## Customization Options

- Modify the default model parameters in the sidebar.
- Change the API endpoint or key by editing `secrets.toml`.
- Customize UI elements by editing Streamlit components.

## Troubleshooting & FAQs

**Q: I am getting an API key error. What should I do?**\
A: Ensure that your `secrets.toml` file contains valid API credentials.

**Q: The response is taking too long. How can I speed it up?**\
A: Lower the `max_tokens` or increase `temperature` for faster response times.

**Q: How can I deploy the app?**\
A: You can deploy it to Streamlit Cloud or a VPS by following Streamlit deployment guides.

## Project Links

- **Project Repository:** `[Add link here]`
- **Live Demo:** `[Add link here]`
- **Documentation:** `[Add link here]`
- **Support/Contact:** `[Add link here]`

