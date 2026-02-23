import streamlit as st
import groq

def run_chatbot(api_key):
    # Gemini Setup
   client=Groq(api_key=api_key)
    model ='llama-3.370b-versatil'

    st.divider()
    st.subheader("Urmila Traders AI Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat history dikhane ke liye
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Input aur AI Response
    if prompt := st.chat_input("Ask me anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                response = model.start_chat().send_message(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:

                st.error(f"Error: {e}")




