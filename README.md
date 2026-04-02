# Warehouse AI Copilot

Warehouse AI Copilot is an AI-powered tool for evaluating warehouse layouts before acquisition or operational planning.

The system analyzes warehouse layout images or PDFs and combines visual analysis with operational parameters to assess whether a facility can support a given fulfillment workload.

It identifies potential operational bottlenecks, evaluates picking and packing efficiency, and provides practical recommendations for improving warehouse operations.

---

## Features

• Warehouse layout analysis from images or PDFs  

• Identification of key operational areas:
- shelving storage zones
- picking aisles
- packing stations
- receiving areas
- shipping docks  

• Operational analysis based on user inputs:
- warehouse size
- orders per day
- items per order
- workforce size

• Detection of operational bottlenecks  
• Picking efficiency evaluation  
• Packing capacity assessment  
• Practical improvement suggestions  
• Warehouse suitability score and recommendation  

---

## How It Works

1. Upload a warehouse layout (image or PDF).
2. The system analyzes the visual layout structure using an AI vision model.
3. The user provides operational parameters such as order volume and workforce size.
4. The system evaluates whether the warehouse layout can support the required throughput and highlights potential risks or improvements.

---

## Technology Stack

- Python
- Streamlit
- OpenAI API
- PyMuPDF
- Pillow
- pdf2image
- reportlab
- python-dotenv

---

## Project Structure

```
warehouse-ai-copilot/

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
```

---

## Example Use Case

A logistics or operations team evaluating a potential warehouse facility can upload a proposed layout and provide operational parameters such as order volume and workforce size.

The system analyzes the layout and provides insights into whether the facility can realistically support the expected fulfillment operations.

---

## Disclaimer

This tool provides AI-assisted operational insights and should be used as a decision-support system rather than a definitive operational assessment.

This tool was built for a private client in the logistics field.