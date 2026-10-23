
import streamlit as st
import time

st.set_page_config(
    page_title="Simple Chatbot",
    layout="centered"
)

st.title("Simple Chatbot")
st.write("Hello! Send me a message to start chatting.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:
    # Save and display the user's message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Generate a demo reply
    with st.chat_message("assistant"):
        with st.spinner("Assistant is typing..."):
            time.sleep(1)

            text = prompt.lower()

            if "python" in text:
                reply = (
                    "Python is a popular programming "
                    "language used in AI and data science."
                )
            elif "streamlit" in text:
                reply = (
                    "Streamlit is a Python framework "
                    "for building interactive web apps."
                )
            elif "hello" in text or "hi" in text:
                reply = "Hello! How can I help you today?"
            elif "your name" in text:
                reply = "I am a simple demo chatbot built with Streamlit."
            else:
                reply = (
                    f"You said: '{prompt}'. "
                    "I am a demo chatbot!"
                )

        st.write(reply)

    # Save the assistant's reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

# Download chat history
st.subheader("Chat History")

if st.session_state.messages:
    chat_text = "\n".join(
        f"{msg['role']}: {msg['content']}"
        for msg in st.session_state.messages
    )

    st.download_button(
        label="Download Chat History",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain"
    )
else:
    st.info("Your conversation will appear here.")

# Clear conversation
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
