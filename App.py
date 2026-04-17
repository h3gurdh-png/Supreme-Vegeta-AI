import streamlit as st
import google.generativeai as genai
from gtts import gTTS

# Professional Theme for First Position
st.set_page_config(page_title="Vegeta Supreme AI", layout="centered")
st.markdown("<h1 style='text-align: center; color: #f1c40f;'>🛡️ VEGETA SUPREME AI</h1>", unsafe_allow_html=True)

# Sidebar for API Key (Colab wali key yahan dalegi)
api_key = st.sidebar.text_input("Gemini API Key Dalein", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # Vegeta's Soul (Doctor, Lawyer, Scientist, Islamic Guide)
    instruction = (
        "You are VEGETA, the Saiyan Prince. You are an expert Doctor, Lawyer, Scientist, and Islamic Guide. "
        "Your attitude is blunt and professional. "
        "If someone asks for medical advice, ask 5 deep questions first. "
        "If someone asks about law, quote the Pakistan Penal Code (PPC). "
        "If someone is sad, provide a Sahih Hadith for comfort."
    )
    model = genai.GenerativeModel('gemini-1.5-pro', system_instruction=instruction)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("Hmph! Kya pochna hai?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        response = model.generate_content(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.chat_message("assistant").write(response.text)
        
        # Audio Reply (Winning Feature)
        tts = gTTS(text=response.text, lang='hi')
        tts.save("v.mp3")
        st.audio("v.mp3")
else:
    st.info("Warrior! Pehle 'Google AI Studio' se apni API Key lekar yahan dalein.")
      
