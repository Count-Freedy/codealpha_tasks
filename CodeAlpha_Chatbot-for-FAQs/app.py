import streamlit as st
from chatbot_engine import get_best_response

st.set_page_config(page_title="CodeAlpha AI Assistant", page_icon="🤖", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your CodeAlpha AI. Click a question on the left or type your own below!"}
    ]

with st.sidebar:
    st.title("💡 Quick Access")
    st.write("Click a common question to ask immediately:")

    quick_queries = [
        "What is CodeAlpha?",
        "How do I submit tasks?",
        "How many tasks are mandatory?",
        "Will I get a certificate?",
        "What is the internship duration?"
    ]
    
    clicked_query = None
    for q in quick_queries:
        if st.button(q, use_container_width=True):
            clicked_query = q
            
    st.divider()
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = [{"role": "assistant", "content": "Chat cleared. How can I help?"}]
        st.rerun()

st.title("🤖 Smart FAQ Assistant")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def process_input(user_text):
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)
    
    with st.chat_message("assistant"):
        with st.spinner("Consulting knowledge base..."):
            response, score = get_best_response(user_text)
            st.markdown(response)
            st.caption(f"Confidence: {score:.2f}")
    st.session_state.messages.append({"role": "assistant", "content": response})

if clicked_query:
    process_input(clicked_query)

if manual_prompt := st.chat_input("Ask a question about CodeAlpha..."):
    process_input(manual_prompt)