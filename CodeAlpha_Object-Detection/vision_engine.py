import cv2
from ultralytics import YOLO

# Load YOLO11 Nano (Optimized for 2026 performance)
model = YOLO('yolo11n.pt') 

# Using a set to keep track of unique IDs globally in this session
unique_track_ids = set()

def detect_track_and_count(frame, conf_threshold=0.5):
    global unique_track_ids
    
    # Run tracking (ByteTrack is built-in)
    results = model.track(frame, persist=True, conf=conf_threshold, tracker="bytetrack.yaml", verbose=False)
    
    # Check if any objects with IDs are detected
    if results[0].boxes.id is not None:
        # Extract IDs as a list of integers
        ids = results[0].boxes.id.int().cpu().tolist()
        
        # Add new IDs to our set (Sets automatically handle duplicates)
        for obj_id in ids:
            unique_track_ids.add(obj_id)
            
        # Draw boxes and IDs on the frame
        annotated_frame = results[0].plot()
        return annotated_frame, len(unique_track_ids)
    
    return frame, len(unique_track_ids)

def reset_counter():
    global unique_track_ids
    unique_track_ids.clear()