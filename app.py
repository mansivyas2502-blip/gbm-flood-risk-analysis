import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from geopy.distance import geodesic
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(page_title="GBM Flood Risk Analysis", layout="wide")

st.title("Flood Risk Analysis in the Ganga–Brahmaputra–Meghna Basin")

st.markdown("""
This application performs a geospatial flood risk assessment of the
Ganga–Brahmaputra–Meghna (GBM) basin using river gauging station danger levels.
""")

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("flood_gauges_gbm.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# -------------------------------------------------
# DATA CLEANING
# -------------------------------------------------
df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
df["Danger Level"] = pd.to_numeric(df["Danger Level"], errors="coerce")

df = df.dropna(subset=["Latitude", "Longitude", "Danger Level"])

# -------------------------------------------------
# FLOOD RISK CLASSIFICATION
# -------------------------------------------------
q75 = df["Danger Level"].quantile(0.75)
q40 = df["Danger Level"].quantile(0.40)

def classify_risk(val):
    if val >= q75:
        return "High"
    elif val >= q40:
        return "Medium"
    else:
        return "Low"

df["Risk"] = df["Danger Level"].apply(classify_risk)

# -------------------------------------------------
# DISTANCE TO HIGH-RISK ZONES
# -------------------------------------------------
high_risk = df[df["Risk"] == "High"]

def nearest_high_risk_distance(row):
    return high_risk.apply(
        lambda hr: geodesic(
            (row["Latitude"], row["Longitude"]),
            (hr["Latitude"], hr["Longitude"])
        ).km,
        axis=1
    ).min()

df["Distance_to_HighRisk_km"] = df.apply(nearest_high_risk_distance, axis=1)

# -------------------------------------------------
# FLOOD RISK INDEX
# -------------------------------------------------
scaler = MinMaxScaler()
df["Danger_norm"] = scaler.fit_transform(df[["Danger Level"]])

df["Distance_norm"] = 1 - (
    df["Distance_to_HighRisk_km"] / df["Distance_to_HighRisk_km"].max()
)

df["Flood_Risk_Index"] = 0.6 * df["Danger_norm"] + 0.4 * df["Distance_norm"]

# -------------------------------------------------
# DBSCAN CLUSTERING (HIGH-RISK ONLY)
# -------------------------------------------------
high_risk = df[df["Risk"] == "High"].copy()
coords = np.radians(high_risk[["Latitude", "Longitude"]])

high_risk["Cluster"] = DBSCAN(
    eps=0.5,
    min_samples=3,
    metric="haversine"
).fit_predict(coords)

# -------------------------------------------------
# MAP CREATION
# -------------------------------------------------
m = folium.Map(location=[26.5, 88.0], zoom_start=6)

risk_colors = {"High": "red", "Medium": "orange", "Low": "green"}

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=6,
        color=risk_colors[row["Risk"]],
        fill=True,
        fill_color=risk_colors[row["Risk"]],
        fill_opacity=0.7,
        popup=f"""
        <b>Station:</b> {row['Station']}<br>
        <b>Risk:</b> {row['Risk']}<br>
        <b>Flood Risk Index:</b> {row['Flood_Risk_Index']:.2f}
        """
    ).add_to(m)

# 50 km influence zones
for _, row in high_risk.iterrows():
    folium.Circle(
        location=[row["Latitude"], row["Longitude"]],
        radius=50000,
        color="red",
        fill=False
    ).add_to(m)

st.subheader("Interactive Flood Risk Map")
folium_static(m, width=1200, height=600)

# -------------------------------------------------
# INTERPRETATION
# -------------------------------------------------
st.markdown("""
### Interpretation
- High-risk stations form spatial clusters along GBM river corridors.
- DBSCAN identifies flood hotspots rather than isolated stations.
- The Flood Risk Index combines severity and spatial proximity.
- 50 km influence zones highlight regions of elevated flood vulnerability.
""")
