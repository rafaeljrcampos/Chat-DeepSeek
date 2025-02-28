import streamlit as st
from langchain_ollama import ChatOllama

def keyWarning():
    placeholder = st.empty()
    key = placeholder.text_input('Enter the localhost port (e.g., 11434).')
    if key:
        placeholder.empty()  # Limpa os elementos visuais
        return key

def chatBot(base_url_local):
    print('oi')
    llm_model = ChatOllama(model='deepseek-r1:7b',base_url=f'http://localhost:{base_url_local}') # Configuração básica

    st.title("How can I help?")

    if 'message' not in st.session_state:
        st.session_state['message'] = []
    messages = st.session_state['message']

    for types, contents in messages:
        chat = st.chat_message(types)
        chat.markdown(contents)

    prompt = st.chat_input('Ask something.')

    if prompt:  # Exibe a mensagem do usuário, para logo em seguida exibir a do Chat-Bot
        messages.append(('human',prompt)) # Otima forma de armazenar memoria no Chat-Bot
        chat = st.chat_message('human')
        chat.markdown(prompt)
        response=llm_model.invoke(messages).content
        messages.append(('ai',response))
        chat = st.chat_message('ai')
        chat.markdown(response)