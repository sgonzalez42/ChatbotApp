import os
import streamlit as st
import toml
from google import genai

secrets_file_path = ".streamlit/secrets.toml"
secrets = toml.load(f'{secrets_file_path}')
os.environ["GEMINI_API_KEY"] = secrets["GEMINI_API_KEY"]

client = genai.Client()

st.title("Chatbot using Gemini AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask a question"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = client.models.generate_content(
    model ="gemini-2.5-flash",
    contents = prompt
)

    reply = response.text

    st.session_state.messages.append({"role":"assistant", "content":reply})
    with st.chat_message("assistant"):
        st.write(reply)