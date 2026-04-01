Warehouse AI Copilot

AI-powered tool for evaluating warehouse layouts before acquisition or operational planning.

This application analyzes warehouse layout images or PDFs and combines visual analysis with operational parameters to assess whether the facility can support a given fulfillment workload.

The system helps identify potential bottlenecks, evaluate picking and packing efficiency, and provide practical recommendations for improving warehouse operations.

Features:
Warehouse layout analysis from images or PDFs
Identification of key operational areas:
shelving storage zones
picking aisles
packing stations
receiving areas
shipping docks
Operational analysis based on:
warehouse size
order volume
items per order
workforce size
Detection of potential operational bottlenecks
Picking and packing efficiency evaluation
Practical improvement suggestions
Warehouse suitability score and recommendation

How It Works:
Upload a warehouse layout (image or PDF).
The AI analyzes the layout structure and workflow.
The user provides operational parameters.
The system evaluates whether the warehouse can support the required throughput.

The analysis includes:
estimated operational capacity
bottlenecks in picking or packing
picking efficiency observations
packing station capacity
improvement suggestions
warehouse suitability score
🛠 Tech Stack
Python
Streamlit
OpenAI API
PyMuPDF
Pillow

Project Structure:
warehouse-ai-copilot
data/
sample_layouts/
src/
app.py
vision.py
analysis.py
prompts.py
utils.py

requirements.txt
README.md


Example Use Case:
A logistics team evaluating a new warehouse facility can upload the proposed layout and input operational parameters such as order volume and workforce size.
The system analyzes the layout and provides insights into whether the warehouse design can realistically support the required fulfillment operations.

Disclaimer
This tool provides AI-assisted operational insights and should be used as a decision-support system rather than a definitive operational assessment.

This project was built for a private client in the logistics field.