import streamlit as st
from groq import Groq  # 'import groq' ki jagah ye zaroori hai

def run_chatbot(api_key):
    # Sahi tarika: Groq client banana
    client = Groq(api_key=api_key)
    st.divider()
    st.subheader("Urmila Traders AI Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                # Groq mein response mangne ka sahi method
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}]
                )
                response = completion.choices[0].message.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Chatbot Error: {e}")


