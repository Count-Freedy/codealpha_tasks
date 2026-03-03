import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from st_copy_to_clipboard import st_copy_to_clipboard
import os

st.set_page_config(page_title="AI Multi-Language Translator", page_icon="🌐", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; transition: 0.3s; }
    .stButton>button:hover { background-color: #ff4b4b; color: white; transform: scale(1.02); }
    .stTextArea>div>div>textarea { font-size: 1.1rem; border-radius: 10px; }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 AI Multi-Language Translator")
st.write("Professional-grade translation for your global communication needs.")

with st.sidebar:
    st.header("⚙️ Configuration")
    langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
    
    source_lang = st.selectbox("Source Language", ["auto"] + list(langs_dict.keys()))
    target_lang = st.selectbox("Target Language", list(langs_dict.keys()), index=27)
    st.divider()
    st.info("Tip: 'Auto' detection works best for short sentences.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input")
    input_text = st.text_area("Source Text", placeholder="Type or paste text here...", height=250, label_visibility="collapsed")

if st.button("🚀 Translate"):
    if not input_text.strip():
        st.error("Please enter some text to translate.")
    else:
        try:
            translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(input_text)
            
            with col2:
                st.subheader("Translation")
                st.text_area("Result", value=translated_text, height=250, label_visibility="collapsed", key="output_box")
                
                st.write("### 🛠️ Quick Tools")
                util_col1, util_col2 = st.columns(2)
                
                with util_col2:
                    st.write("📋 Copy Text")
                    st_copy_to_clipboard(translated_text)
                
        except Exception as e:
            st.error(f"Translation Error: {e}")

st.markdown("---")
st.markdown(f"<p style='text-align: center; color: grey;'>Developed by <b>Kunal Kumar</b>", unsafe_allow_html=True)