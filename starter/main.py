import streamlit as st
from chatbot_config import keyWarning,chatBot
st.set_page_config(page_title='Chat-Bot 💾', layout='centered')

if 'urlKey' not in st.session_state:
    key = keyWarning()
    if key:
        st.session_state['urlKey'] = str(key)

if 'urlKey' in st.session_state:
    chatBot(st.session_state['urlKey'])