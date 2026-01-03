# Flood Risk Analysis in the Ganga–Brahmaputra–Meghna Basin

This project presents a geospatial flood risk assessment of the
Ganga–Brahmaputra–Meghna (GBM) basin using river gauging station danger level data.

## Objectives
- Visualize spatial distribution of flood risk across the GBM basin
- Classify gauging stations into low, medium, and high flood risk categories
- Identify high-risk flood zones based on extreme danger levels
- Analyze proximity of stations to high-risk zones using distance-based methods
- Detect spatial flood hotspots using DBSCAN clustering
- Develop an interactive Streamlit web application

## Dataset
The dataset consists of river gauging stations with geographic coordinates,
danger levels, river information, and basin classification.
Only GBM basin stations are included.

## Methodology
Geospatial preprocessing, percentile-based risk classification,
geodesic distance analysis, flood risk index computation,
and density-based spatial clustering (DBSCAN) were applied.

## Technologies Used
Python, Pandas, NumPy, Geopy, Folium, Streamlit, Scikit-learn

## How to Run Locally

