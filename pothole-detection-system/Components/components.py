import streamlit as st

def add_header():
    st.markdown(
        """
        <div style='background-color:#004466;padding:12px;border-radius:6px;margin-bottom:20px'>
            <h2 style='color:white;text-align:center'>🕳️ Pothole Dimension Detection System</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

def add_footer():
    st.markdown(
        """
        <hr style="margin-top:40px">
        <div style='text-align:center; color:gray; font-size:13px'>
            Made with ❤️ for VTU Major Project 2025 | YOLOv8 | FastAPI | Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )
