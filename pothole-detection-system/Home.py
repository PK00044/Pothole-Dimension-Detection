from pathlib import Path
import re
import streamlit as st
from Components.components import add_header, add_footer

st.set_page_config(page_title="Pothole Detection System", layout="centered", page_icon="🕳️")
add_header()

st.title("Welcome to Pothole Detection App")

home_path = Path("home.md")
md_text = home_path.read_text(encoding="utf-8")


def render_markdown_with_images(md):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    parts = re.split(pattern, md)

    i = 0
    while i < len(parts):
        st.markdown(parts[i], unsafe_allow_html=True)
        if i + 2 < len(parts):
            alt = parts[i + 1]
            img_path = parts[i + 2]
            st.image(img_path, caption=alt, use_column_width=True)
        i += 3


render_markdown_with_images(md_text)

add_footer()