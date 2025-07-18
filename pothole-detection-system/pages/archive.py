# pages/archive.py
import streamlit as st
import os
from PIL import Image
import json
import datetime

st.set_page_config(page_title="📂 Archive Viewer", layout="wide")
st.title("📂 Media Archive Viewer")
st.markdown("Browse previously scanned images/videos along with metadata and download options.")

ARCHIVE_DIR = "Storage/archives"

# Load metadata
metadata_path = os.path.join(ARCHIVE_DIR, "metadata.json")
if os.path.exists(metadata_path):
    with open(metadata_path, "r") as f:
        metadata = json.load(f)
else:
    st.warning("No metadata found.")
    metadata = []

# Filter options
media_type = st.radio("Filter by media type:", ["All", "Image", "Video"], horizontal=True)
filtered = metadata if media_type == "All" else [m for m in metadata if m["type"] == media_type.lower()]

# Sort by most recent
filtered = sorted(filtered, key=lambda x: x["timestamp"], reverse=True)

# Display
for item in filtered:
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write(f"📅 Date: {item['timestamp']}")
        st.write(f"🕳️ Potholes Detected: {item['count']}")
        st.write(f"📁 Type: {item['type'].capitalize()}")
    with col2:
        media_path = os.path.join(ARCHIVE_DIR, item["filename"])
        if item["type"] == "image":
            st.image(media_path, width=300)
        else:
            st.video(media_path)
        with open(media_path, "rb") as f:
            st.download_button(
                label="📥 Download",
                data=f,
                file_name=item["filename"],
                mime="image/jpeg" if item["type"] == "image" else "video/mp4"
            )
