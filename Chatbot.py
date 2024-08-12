from openai import OpenAI
import os

import streamlit as st

openai_api_key = os.getenv("OPENAI_API_KEY")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Twitter-like!")
st.caption("🚀 Turn your text into English in a Twitter-like way!")

st.session_state["messages"] = [{"role": "assistant", "content": "Translate user's input into English!"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

st.session_state["messages"] = [{"role": "assistant", "content": 
                                 """
                                 Translate user's input into English\
                                  in a twitter-like way and a common way!\
                                  Tag at the beginning of your outputs\
                                  with '[twitter-like] ' or '[common] '.\
                                 between the 2 type of answers, insert a new line."
                                  """
                                  }]

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
