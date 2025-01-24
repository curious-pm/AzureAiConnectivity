import streamlit as st
import requests
import json
import time
from typing import Dict, Any, Iterator

class AzureOpenAIChat:
    def __init__(self):
        # Retrieve API credentials from Streamlit secrets
        self.API_ENDPOINT = st.secrets.get("AZURE_OPENAI_API_ENDPOINT", "")
        self.API_KEY = st.secrets.get("AZURE_OPENAI_API_KEY", "")  

        # Ensure API key is available
        if not self.API_KEY:
            raise ValueError("Azure OpenAI API Key is missing.")

    def generate_response_stream(
        self,
        query: str,
        max_tokens: int = 1000,
        temperature: float = 0.7,
        top_p: float = 1.0,
        frequency_penalty: float = 0.0,
        presence_penalty: float = 0.0
    ) -> Iterator[str]:
        """Generate streaming response from Azure OpenAI"""
        headers = {
            "Content-Type": "application/json",
            "api-key": self.API_KEY,
        }

        # Define request payload
        data = {
            "messages": [{"role": "user", "content": query}],
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
            "stream": True  # Enable streaming mode
        }

        try:
            # Make a POST request to the Azure OpenAI endpoint
            response = requests.post(
                self.API_ENDPOINT,
                headers=headers,
                json=data,
                stream=True
            )
            response.raise_for_status()

            # Process the response stream line by line
            for line in response.iter_lines():
                if line.strip() == b'data: [DONE]':
                    break
                if line.startswith(b'data: '):
                    json_str = line[6:].decode('utf-8')
                    try:
                        json_data = json.loads(json_str)
                        if 'choices' in json_data and len(json_data['choices']) > 0:
                            delta = json_data['choices'][0].get('delta', {})
                            if 'content' in delta:
                                yield delta['content']
                    except (json.JSONDecodeError, IndexError, KeyError):
                        continue
        except requests.exceptions.RequestException as req_err:
            raise RuntimeError(f"Request error: {req_err}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error: {str(e)}")

def main():
    st.set_page_config(page_title="Azure AI Chat", page_icon="\U0001F4AC")
    st.title("Azure Ai Connectivity")

    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Sidebar for configuring model parameters
    with st.sidebar:
        st.header("Model Parameters")

        # Store default and current parameter values in session state
        if "parameters" not in st.session_state:
            st.session_state.parameters = {
                "temperature": 0.7,
                "top_p": 1.0,
                "frequency_penalty": 0.0,
                "presence_penalty": 0.0,
            }
            st.session_state.default_parameters = st.session_state.parameters.copy()

        # UI sliders for model parameters
        temperature = st.slider("Temperature", 0.0, 2.0, st.session_state.parameters["temperature"], 0.1)
        top_p = st.slider("Top P", 0.0, 1.0, st.session_state.parameters["top_p"], 0.1)
        frequency_penalty = st.slider("Frequency Penalty", 0.0, 2.0, st.session_state.parameters["frequency_penalty"], 0.1)
        presence_penalty = st.slider("Presence Penalty", 0.0, 2.0, st.session_state.parameters["presence_penalty"], 0.1)

        # Update session state when sliders change
        st.session_state.parameters.update({
            "temperature": temperature,
            "top_p": top_p,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
        })

        # Reset to default values button
        if st.button("Reset to Defaults"):
            st.session_state.parameters = st.session_state.default_parameters.copy()
            st.experimental_set_query_params(_=int(time.time()))

        # Explanation of parameters
        st.write("---")
        st.write("### Parameter Descriptions:")
        st.write("**Temperature:** Increase randomness of the response.")
        st.write("**Top P:** Limit the response to top probability tokens (nucleus sampling).")
        st.write("**Frequency Penalty:** Penalize repeated tokens to reduce redundancy.")
        st.write("**Presence Penalty:** Encourage diverse topics by penalizing existing tokens.")

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input field
    if prompt := st.chat_input("Enter your message"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        chat_client = AzureOpenAIChat()

        # Display response with real-time updates
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            try:
                for text_chunk in chat_client.generate_response_stream(
                    prompt,
                    max_tokens=1000,
                    temperature=st.session_state.parameters["temperature"],
                    top_p=st.session_state.parameters["top_p"],
                    frequency_penalty=st.session_state.parameters["frequency_penalty"],
                    presence_penalty=st.session_state.parameters["presence_penalty"],
                ):
                    full_response += text_chunk
                    response_placeholder.markdown(full_response + "▌")
                response_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except RuntimeError as err:
                st.error(f"Error generating response: {err}")
                response_placeholder.markdown("Sorry, I couldn't generate a response.")

if __name__ == "__main__":
    main()
