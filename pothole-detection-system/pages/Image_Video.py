import sys
import base64
import io
import requests
from PIL import Image
import streamlit as st
from Components.components import add_header, add_footer


add_header()
st.title("🖼️ Upload Image/Video for Detection")
st.markdown("Upload an image or video to detect potholes and estimate their dimensions.")

uploaded_file = st.file_uploader("Choose an image or video", type=["jpg", "jpeg", "png", "mp4"])

if uploaded_file is not None:
    if uploaded_file.type.startswith("image"):
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    elif uploaded_file.type.startswith("video"):
        st.video(uploaded_file)

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    with st.spinner("Detecting potholes..."):
        try:
            response = requests.post("http://127.0.0.1:8000/detect", files=files)

            if response.status_code == 200:
                if uploaded_file.type.startswith("image"):
                    result = response.json()
                    if "processed_image" in result:
                        img_base64 = result["processed_image"]
                        img_bytes = base64.b64decode(img_base64)
                        image = Image.open(io.BytesIO(img_bytes))
                        st.image(image, caption="Detected Image", use_column_width=True)
                        st.success(f"Detection complete! Potholes detected: {result['pothole_count']}")
                    else:
                        st.error("No image returned. Server said: " + str(result))
                elif uploaded_file.type.startswith("video"):
                    output_path = "output.mp4"
                    with open(output_path, "wb") as f:
                        f.write(response.content)
                    pothole_count = int(response.headers.get("x-pothole-count", 0))
                    st.success(f"Detection complete! Potholes detected: {pothole_count}")
                    st.video(output_path)
                    with open(output_path, "rb") as f:
                        st.download_button(
                            label="📥 Download Processed Video",
                            data=f,
                            file_name="detected_potholes.mp4",
                            mime="video/mp4"
                        )
            else:
                st.error("Detection failed: " + response.text)

        except Exception as e:
            st.error(f"Request failed: {e}")


add_footer()