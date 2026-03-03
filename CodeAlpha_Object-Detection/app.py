import streamlit as st
import cv2
from vision_engine import detect_track_and_count, reset_counter

st.set_page_config(page_title="AI Object Tracker & Counter", layout="wide")

st.title("🎯 Real-Time Object Tracking & Counting")
st.write("This system assigns unique IDs to objects and counts total unique detections.")

# --- SIDEBAR ---
with st.sidebar:
    st.header("Control Panel")
    conf_val = st.slider("Confidence Threshold", 0.1, 1.0, 0.4)
    run = st.toggle("Start Camera", value=False)
    
    if st.button("🔄 Reset Total Count"):
        reset_counter()
        st.success("Counter reset!")
    
    st.divider()
    st.info("Note: The counter tracks total unique objects seen since the start or last reset.")

# --- MAIN LAYOUT ---
col1, col2 = st.columns([3, 1])

with col2:
    st.subheader("Live Stats")
    count_placeholder = st.empty() # Dynamic placeholder for the number

with col1:
    FRAME_WINDOW = st.image([])

# --- CAMERA LOGIC ---
if run:
    camera = cv2.VideoCapture(0) # 0 for default webcam
    
    while run:
        success, frame = camera.read()
        if not success:
            st.error("Webcam not found or busy.")
            break
            
        # Convert BGR to RGB for Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # AI Processing
        processed_frame, total_count = detect_track_and_count(frame, conf_val)
        
        # Update UI components
        FRAME_WINDOW.image(processed_frame)
        count_placeholder.metric("Total Unique Objects", total_count)
        
    camera.release()
else:
    st.warning("Camera is currently OFF. Use the sidebar to start.")