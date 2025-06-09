import streamlit as st

st.title("📘 Tutor Bot")
st.caption("An AI-powered tutor to help you understand concepts step-by-step.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        ["assistant", "👋 Hello! I'm your AI tutor. Ask me anything you’d like to learn."]
    ]

# Display chat history
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

if user_input := st.chat_input(placeholder="Type your message here..."):
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append(["user", user_input])
    
    ml_response = f"This is a mock response from the AI: {user_input[::-1]}"
    st.session_state.chat_history.append(["ai", ml_response])
    
    st.chat_message("ai").write(ml_response)
    
    ml_response = f"This is a placeholder response. For demonstration, your input reversed is: {user_input[::-1]}"
# Optional: Reset chat button
with st.sidebar:
    if st.button("🔄 Reset Conversation"):
        st.session_state.chat_history = [
            ["assistant", "👋 Hello! I'm your AI tutor. Ask me anything you’d like to learn."]
        ]


