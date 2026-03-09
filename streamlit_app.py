import streamlit as st
import google.generativeai as genai
from gtts import gTTS

# --- CONFIG ---
genai.configure(api_key="AIzaSyBx0JcxfZA8cs2eSwA1uWclTp5K-jpYOqg")
APP_PASSWORD = "UP16" 

# --- LOCK SYSTEM ---
if "locked" not in st.session_state:
    st.session_state["locked"] = True

if st.session_state["locked"]:
    st.title("🔐 AI Studio: Entry Password")
    pwd = st.text_input("Password daalein (UP16):", type="password")
    if st.button("Unlock Engine"):
        if pwd == APP_PASSWORD:
            st.session_state["locked"] = False
            st.rerun()
        else:
            st.error("Galat Password!")
    st.stop()

# --- MAIN APP ---
st.title("🤖 Titan AI: Digital Production")
st.write("Apna topic likhein aur AI Avatar ke sath video banayein.")

topic = st.text_input("Aapka Topic:", placeholder="Ex: Future Robots in India...")

if st.button("🚀 Start Making Video"):
    if topic:
        model = genai.GenerativeModel('gemini-pro')
        with st.status("⚙️ AI Kaam kar raha hai...", expanded=True):
            # 1. Avatar Design
            st.subheader("🎭 AI Avatar & Character Look")
            res = model.generate_content(f"Describe a unique 100% AI avatar/person for: {topic}. No real humans.")
            st.info(res.text)
            
            # 2. Script
            st.subheader("📝 Viral Script")
            s_res = model.generate_content(f"Write a 1-minute viral video script in Hindi/English for an AI Avatar on: {topic}")
            st.write(s_res.text)
            
            # 3. Voice
            st.subheader("🔊 Audio Voice-over")
            tts = gTTS(text=s_res.text[:300], lang='hi')
            tts.save("voice.mp3")
            st.audio("voice.mp3")
            
        st.balloons()
        st.success("Kaam ho gaya! ✅")
    else:
        st.error("Pehle topic likhiye!")
