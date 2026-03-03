import json
import torch
import streamlit as st
from sentence_transformers import SentenceTransformer, util

@st.cache_resource
def load_ai_model():
    """Loads the model once and keeps it in memory for the whole session."""
    return SentenceTransformer('all-MiniLM-L6-v2')

@st.cache_data
def load_faqs():
    """Loads the FAQ database once from the local JSON file."""
    with open('faqs.json', 'r') as f:
        return json.load(f)

def get_best_response(user_query):
    model = load_ai_model()
    faqs = load_faqs()
    
    questions = [item['question'] for item in faqs]
    
    query_embedding = model.encode(user_query, convert_to_tensor=True)
    faq_embeddings = model.encode(questions, convert_to_tensor=True)
    
    scores = util.cos_sim(query_embedding, faq_embeddings)[0]
    
    best_idx = torch.argmax(scores).item()
    confidence = scores[best_idx].item()

    if confidence > 0.45:
        return faqs[best_idx]['answer'], confidence
    else:
        return "I'm not quite sure about that. Could you try rephrasing or contact support at info@codealpha.com?", confidence