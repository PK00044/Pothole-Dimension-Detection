import streamlit as st
import os
import sys
from Components.components import add_header, add_footer

add_header()
sys.path.append(os.path.join(os.getcwd(), "backend", "app"))
from realtime_detector import run_realtime

st.title("🔴 Real-time Pothole Detection")

cam_choice = st.radio("Select Camera Source", ["PC Webcam", "Mobile Camera (DroidCam)"])
start_button = st.button("Start Detection")

if start_button:
    st.warning("Press 'q' in the terminal window to stop the webcam feed.")
    if cam_choice == "PC Webcam":
        run_realtime(0)
    else:
        run_realtime("http://192.168.137.111:4747/video")  # DroidCam IP


add_footer()