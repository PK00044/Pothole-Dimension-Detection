import streamlit as st
import requests
import pandas as pd
import json
import plotly.express as px
import streamlit as st
from Components.components import add_header, add_footer


add_header()
st.title("📊 Detection Dashboard")
st.markdown("This dashboard displays the total number of processed files and detected potholes.")

# --- Fetch stats (totals) ---
try:
    response = requests.get("http://127.0.0.1:8000/stats")
    if response.status_code == 200:
        data = response.json()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("🖼️ Images Scanned", data["image_scanned"])
            st.metric("🕳️ Potholes in Images", data["potholes_in_images"])
        with col2:
            st.metric("🎞️ Videos Scanned", data["video_scanned"])
            st.metric("🕳️ Potholes in Videos", data["potholes_in_videos"])
    else:
        st.error("Failed to fetch stats from backend.")
except Exception as e:
    st.error(f"Error fetching stats: {e}")

# --- Load full logs for tables & charts ---
logs = []
try:
    log_response = requests.get("http://127.0.0.1:8000/logs")
    if log_response.status_code == 200:
        logs = log_response.json()
except Exception as e:
    st.error(f"Error loading logs: {e}")

# --- Show recent detections (Last 5) ---
st.markdown("---")
st.subheader("🕒 Recent Detections (Last 5)")

if logs:
    df_logs = pd.DataFrame(logs)
    st.dataframe(df_logs.tail(5).iloc[::-1])  # last 5, reversed
else:
    st.info("No detection logs available yet.")

# --- 📈 Detection Trends ---
st.markdown("---")
st.subheader("📈 Detection Trends")

if logs:
    df_logs = pd.DataFrame(logs)
    df_logs['timestamp'] = pd.to_datetime(df_logs['timestamp'])
    df_logs['date'] = df_logs['timestamp'].dt.date

    # 1. Potholes Per Day (Line Chart)
    daily_potholes = df_logs.groupby('date', as_index=False)['potholes_detected'].sum()
    st.write("Grouped Daily Pothole Data:")
    st.dataframe(daily_potholes)

    daily_potholes['date'] = daily_potholes['date'].astype(str)  # Convert to string for clean axis

    fig1 = px.line(
        daily_potholes,
        x='date',
        y='potholes_detected',
        title="📅 Potholes Detected Per Day",
        markers=True,
        labels={'date': 'Date', 'potholes_detected': 'Potholes'}
    )

    st.plotly_chart(fig1, use_container_width=True)

    # 2. Image vs Video (Pie Chart)
    type_counts = df_logs['file_type'].value_counts().reset_index()
    type_counts.columns = ['Type', 'Count']
    fig2 = px.pie(type_counts, names='Type', values='Count', title='📷 Image vs 🎞️ Video Files')
    st.plotly_chart(fig2, use_container_width=True)

    # 3. Daily Upload Count (Bar Chart)
    daily_uploads = df_logs.groupby('date', as_index=False)['file_type'].count()
    daily_uploads.columns = ['Date', 'Upload Count']
    fig3 = px.bar(daily_uploads, x='Date', y='Upload Count', title='📊 Daily Detection Uploads')
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("Charts will appear once detection logs are available.")

# --- 📥 Download Logs as CSV ---
if logs:
    df_full = pd.DataFrame(logs)
    csv_logs = df_full.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download All Logs as CSV", data=csv_logs, file_name="detection_logs.csv", mime="text/csv")

# --- 📤 Session Summary Download ---
st.markdown("---")
st.subheader("📤 Session Summary Download")

try:
    stats_response = requests.get("http://127.0.0.1:8000/stats")
    if stats_response.status_code == 200:
        stats = stats_response.json()

        # JSON Download
        json_bytes = json.dumps(stats, indent=4).encode("utf-8")
        st.download_button("📥 Download Summary as JSON", json_bytes, file_name="session_summary.json", mime="application/json")

        # CSV Download
        df_stats = pd.DataFrame([stats])
        csv_stats = df_stats.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Summary as CSV", csv_stats, file_name="session_summary.csv", mime="text/csv")

except Exception as e:
    st.error(f"Error generating summary downloads: {e}")

add_footer()