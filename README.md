Geospatial Flood Risk Assessment in the Ganga–Brahmaputra–Meghna (GBM) Basin
Introduction
Flooding is a recurrent hydrological hazard in the Ganga–Brahmaputra–Meghna (GBM) basin, driven by intense monsoonal precipitation, complex river networks, and low‑lying floodplains. The basin experiences frequent overbank flooding, resulting in widespread socio‑economic and environmental impacts. Accurate spatial identification of flood‑prone regions is therefore essential for effective flood preparedness, mitigation planning, and decision support.

This project conducts a geospatial flood risk assessment of the GBM basin using river gauging station danger level data. By integrating spatial analysis, proximity‑based risk evaluation, and density‑based clustering, the study identifies flood hotspots and regions of elevated vulnerability. The results are presented through an interactive Streamlit web application, enabling intuitive exploration of spatial flood risk patterns.

Objectives
The primary objectives of this study are to:

Spatially visualize flood danger levels across gauging stations in the GBM basin

Classify gauging stations into low, medium, and high flood risk categories

Delineate high‑risk flood zones based on extreme danger level thresholds

Quantify the spatial influence of high‑risk zones using geodesic distance analysis

Identify spatial flood hotspots through density‑based clustering (DBSCAN)

Develop an interactive web‑based visualization for analytical and academic use

Study Area
The analysis is strictly confined to the Ganga–Brahmaputra–Meghna (GBM) basin, one of the largest and most flood‑prone river systems in the world. All gauging stations outside the GBM basin were excluded to maintain spatial consistency and analytical relevance. The basin spans multiple hydrological sub‑systems, making it well‑suited for regional‑scale geospatial flood analysis.

Dataset Description
The dataset consists of river gauging station records compiled from authoritative flood monitoring sources. Each station record includes the following key attributes:

Station name

Geographic coordinates (latitude and longitude)

River and tributary information

Basin classification

Recorded danger level values

The dataset was filtered to retain only GBM basin stations. Data were processed in CSV format using Python‑based geospatial and analytical libraries.

Methodology
Data Preprocessing
Latitude, longitude, and danger level values were converted to numeric format

Records with missing or invalid spatial coordinates were removed

Non‑GBM basin stations were filtered out to ensure spatial accuracy

Flood Risk Classification
Flood risk was classified using percentile‑based thresholds derived from danger level values:

High Risk – stations exceeding the upper percentile threshold

Medium Risk – stations with moderate danger levels

Low Risk – stations with comparatively lower danger levels

This approach ensures relative risk differentiation across the basin.

Proximity‑Based Flood Influence Analysis
High‑risk stations were treated as flood‑prone zones. Geodesic distance calculations were performed to measure the distance of each gauging station from the nearest high‑risk zone. A 50 km distance threshold was applied to identify stations falling within the spatial influence of high‑risk flood areas.

Flood Risk Index Development
A composite Flood Risk Index was computed by integrating:

Normalized danger level values

Inverse normalized distance to high‑risk zones

This index provides a continuous measure of flood severity, capturing both hydrological intensity and spatial proximity.

Spatial Clustering (DBSCAN)
Density‑Based Spatial Clustering of Applications with Noise (DBSCAN) was applied to high‑risk stations to detect spatial flood hotspots. This method identifies clusters of elevated flood risk without imposing predefined cluster shapes, making it suitable for irregular river‑based spatial patterns.

Geospatial Visualization
Interactive maps were generated using Folium and embedded within a Streamlit application. Flood risk categories are visualized using color‑coded markers, while influence zones around high‑risk stations are represented using buffer circles to enhance spatial interpretation.

Streamlit Web Application
An interactive web application was developed using Streamlit to present the geospatial analysis results.

Key Features
Interactive flood risk map of the GBM basin

Visual differentiation of low, medium, and high risk zones

50 km influence buffers around high‑risk flood areas

Display of Flood Risk Index values for each station

User‑friendly interface for analytical and academic exploration

Technologies Used
Python

Pandas – data preprocessing and handling

NumPy – numerical computations

Geopy – geodesic distance calculations

Scikit‑learn – DBSCAN spatial clustering

Folium – interactive geospatial visualization

Streamlit – web application development and deployment

Project Structure
gbm-flood-risk-analysis/
│
├── app.py                  # Streamlit application code
├── flood_gauges_gbm.csv     # GBM basin gauging station dataset
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore
Key Findings
High flood risk stations exhibit distinct spatial clustering along major river corridors

Several stations fall within 50 km of high‑risk zones, indicating elevated vulnerability

DBSCAN clustering highlights persistent flood hotspots rather than isolated risk locations

Proximity‑based analysis enhances flood risk interpretation beyond station‑level danger values

Conclusion
This study demonstrates the effectiveness of geospatial techniques for flood risk assessment using gauging station data. By integrating spatial classification, proximity analysis, composite risk indexing, and clustering, the project provides a comprehensive regional‑scale understanding of flood vulnerability within the GBM basin. The interactive Streamlit visualization further enhances interpretability and supports spatial decision‑making in flood preparedness contexts.

Academic Note
This project was developed as part of an academic geospatial analytics assignment and is intended for educational and analytical purposes only.

