
import streamlit as st
import numpy as np
import joblib

# Load KMeans model
kmeans = joblib.load("kmeans_model.pkl")

# Cluster descriptions
cluster_descriptions = {
    1: "Medium income, average spenders",
    2: "High income, high spenders",
    3: "High income, low spenders",
    4: "Low income, low spenders",
    5: "Low income, high spenders",
}

# Page config
st.set_page_config(page_title="Mall Segmentation", page_icon="🛍️", layout="centered")

# Custom CSS for dark mode
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            background-color: #0E1117;
            color: #FAFAFA;
            font-family: 'Segoe UI', sans-serif;
        }
        .stSlider > div {
            color: #1E90FF;  /* Blue slider color */
        }
        .stButton>button {
            background-color: #1E90FF;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5em 1em;
        }
        .stButton>button:hover {
            background-color: #1C86EE;
            color: white;
        }
        .stSuccess {
            background-color: #144620;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)


# Title
st.title("🛍️ Mall Customer Segmentation")
st.write("### Enter customer features to predict segment:")

# Input sliders
income = st.slider("Annual Income (k$)", 15, 150, 60)
score = st.slider("Spending Score (1-100)", 1, 100, 50)

# Predict button
if st.button("🎯 Predict Segment"):
    input_data = np.array([[income, score]])
    cluster = kmeans.predict(input_data)[0]
    description = cluster_descriptions.get(cluster, "Unknown")

    st.success(f"✅ **Predicted Cluster:** {cluster}")
    st.write(f"**🧩 Segment Description:** {description}")
