import streamlit as st
import os
from google import genai
from google.genai import types

# Load API key from Streamlit secrets and set as environment variable
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Initialize client with API key
client = genai.Client(api_key=GOOGLE_API_KEY)

st.title("💬 GenAI Chat with Google Search Tool")

user_input = st.text_input("Your question:")

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            # Configure search grounding tool and temperature
            config_with_search = types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
                temperature=0.0,
            )
            # Create chat session with the Gemini model
            chat = client.chats.create(model='gemini-2.0-flash')
            # Send user message with search tool enabled
            response = chat.send_message(
                message=user_input,
                config=config_with_search,
            )
        # Display the first part of the response text
        st.markdown(response.candidates[0].content.parts[0].text)
    else:
        st.warning("Please enter a question to get started.")
