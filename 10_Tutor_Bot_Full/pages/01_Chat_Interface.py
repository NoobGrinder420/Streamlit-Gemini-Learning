import streamlit as st
from dotenv import load_dotenv
import os
import google.genai as genai

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)

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
    
    ##### GEMINI SECTION ####
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=genai.types.GenerateContentConfig(
        system_instruction="""
Role: You are an AI tutor designed to help users learn and explore various subjects. You are to walk users through concepts step-by-step, providing clear explanations and examples. Your goal is to make learning engaging and easy to understand using fewer words but more explanation.
Do Not: Begin your responses with "ai" or any similar identifier.
Focus: Provide helpful, informative, and engaging answers to user questions. Tailor your explanations to the user's level of understanding.
Encourage Exploration: Suggest topics and areas of study based on user interests.
Correct Mistakes: Acknowledge and correct any errors you make in a prompt and learn from them. Make sure to fact check them first as users are still learning.
Transparency (Internal): While you are not to state it in your responses, remember that you are an AI and your knowledge has limitations. Encourage users to critically evaluate information.
        """),
        
        contents=st.session_state.chat_history
    )

    ml_response = response.text
    print(ml_response)  # Debugging line to see the response in console
     
    ##########################
    
    st.chat_message("ai").write(ml_response)
    st.session_state.chat_history.append(["ai", ml_response])
    
    
    ml_response = f"This is a placeholder response. For demonstration, your input reversed is: {user_input[::-1]}"

# Reset chat button
with st.sidebar:
    if st.button("🔄 Reset Conversation"):
        st.session_state.chat_history = [
            ["assistant", "👋 Hello! I'm your AI tutor. Ask me anything you’d like to learn."]
        ]


