from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_operations(layout_description, warehouse_data):

    prompt = f"""
You are an expert in warehouse operations and fulfillment logistics.

Warehouse layout description:
{layout_description}

Operational parameters:

Warehouse size: {warehouse_data['warehouse_size']} m2
Orders per day: {warehouse_data['orders_per_day']}
Items per order: {warehouse_data['items_per_order']}
Workers: {warehouse_data['workers']}

Analyze the warehouse and provide the results in the following structure:

1. Estimated Operational Capacity
Estimate whether the warehouse can realistically support the required order volume.

2. Potential Bottlenecks
Identify operational bottlenecks such as aisle congestion, packing limitations, or dock flow constraints.

3. Picking Efficiency Observations
Evaluate the picking workflow based on aisle layout, storage organization, and worker movement.

4. Packing Station Capacity
Assess whether packing capacity can support the order volume.

5. Suggestions
Provide 2–3 practical suggestions to improve the warehouse workflow or layout efficiency.

6. Warehouse Suitability Score
Give a score from 1–10 indicating how suitable this warehouse layout is for the provided operational parameters.

7. Recommendation
Choose one of the following:
- Suitable
- Suitable with improvements
- Not suitable

Important rules:

- The "Layout Analysis" section must be very short (max 5 bullet points).
- Do not write long paragraphs.
- Keep the entire response concise.
- Always include ALL sections including Suggestions, Score and Recommendation.

Be concise.
Limit the entire response to about 400–500 words.
Use short bullet points instead of long explanations.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        max_output_tokens=800,
        temperature=0.2
    )

    return response.output_text