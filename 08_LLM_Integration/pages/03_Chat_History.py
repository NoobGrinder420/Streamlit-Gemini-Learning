import streamlit as st

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    # [["user", "hi"], ["ai","hello"]]

st.title("Chat with History")

# Display chat history
for message in st.session_state.chat_history:
    name = message[0]
    frame = message[1]
    
    st.chat_message(name=name).write(f"{frame}")


if user_input := st.chat_input(placeholder="Type your message here..."):
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append(["user", user_input])
    
    ml_response = f"This is a mock response from the AI: {user_input[::-1]}"
    st.session_state.chat_history.append(["ai", ml_response])
    
    st.chat_message("ai").write(ml_response)
    
    