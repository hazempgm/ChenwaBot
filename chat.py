from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import streamlit as st
import os


groq_api_key = os.getenv("GROQ_API_KEY")
chat = ChatGroq(temperature=1, groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")

st.title("Chenwa bot")

with st.sidebar:
    api_key = st.text_input("API Key", key="", type="password")

if "inc" not in st.session_state:
    st.session_state.inc = 0
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "ai", "content": "Hello, how can I help you today?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

def increment():
    st.session_state.inc *= 2

system = """
You are a helpful ai assistant, that excells at computer science and all about computer science
"""

# st.button('PRESS MEE !!', on_click=increment)


# st.write(st.session_state.inc)


if prompt := st.chat_input("Type a message...", key="prompt"):
    st.chat_message("User").write(prompt)
    st.session_state.messages.append({"role": "human", "content": prompt})
    p = ChatPromptTemplate.from_messages([("system", "You are a helpful ai assistant, that excells at computer science and all about computer science")] + [(x["role"], x["content"]) for x in st.session_state.messages])

    chain = p | chat

    response = chain.invoke({"text": prompt})
    st.session_state.messages.append({"role": "ai", "content": response.content})
    st.rerun()

# chain = prompt | chat
# print(chain.invoke({"text": "explain to solve the rhiemand hypothosis."}).content)