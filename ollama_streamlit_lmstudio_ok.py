import streamlit as st
import openai

client = openai.Client(base_url="http://127.0.0.1:1234/v1", api_key="sk-1234")
model = "meta-llama-3.1-8b-instruct"

if "model" not in st.session_state:
    st.session_state["model"] = model

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask your question"):
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state["messages"].append({"role": "user", "content": prompt})

    full_response = ""
    placeholder = st.empty()
    # model = st.session_state["model"]

    response = client.chat.completions.create(model=model, messages=st.session_state["messages"],stream=True)
    # response = ollama.chat(model=model, messages=st.session_state["messages"], stream=True)

    for chunk in response:
        if chunk:
            full_response += chunk.choices[0].delta.content
            placeholder.markdown(full_response + "|")
        placeholder.markdown(full_response)
    st.session_state["messages"].append({"role": "assistant", "content": full_response})