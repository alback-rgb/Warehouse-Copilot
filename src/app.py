import streamlit as st
from PIL import Image

from vision import analyze_layout
from analysis import analyze_operations
from utils import pdf_to_image_bytes
from utils import create_pdf_report

st.set_page_config(page_title="Warehouse Layout Copilot", layout="wide")

st.title("📦 Warehouse Layout Copilot")

st.write(
    "Upload one or two warehouse layouts and let AI analyze the operational structure."
)

# ----------------------------
# Upload Layout
# ----------------------------

uploaded_files = st.file_uploader(
    "Upload warehouse layout",
    type=["png", "jpg", "jpeg", "pdf"],
    accept_multiple_files=True
)

image_bytes_list = []

if uploaded_files:

    if len(uploaded_files) > 2:
        st.warning("Please upload a maximum of 2 files.")
        st.stop()

    for uploaded_file in uploaded_files:

        file_bytes = uploaded_file.getvalue()

        if uploaded_file.type == "application/pdf":

            image_bytes = pdf_to_image_bytes(file_bytes)

            st.info(f"{uploaded_file.name} detected as PDF — analyzing first page.")

            st.image(
                image_bytes,
                caption=f"{uploaded_file.name} (page 1)",
                use_container_width=True
            )

        else:

            image = Image.open(uploaded_file)

            image_bytes = file_bytes

            st.image(
                image,
                caption=f"Uploaded Layout - {uploaded_file.name}",
                use_container_width=True
            )

        image_bytes_list.append(image_bytes)

# ----------------------------
# Warehouse Operational Data
# ----------------------------

st.divider()
st.subheader("Warehouse Operational Data")

col1, col2 = st.columns(2)

with col1:

    warehouse_size = st.number_input(
        "Warehouse size (m²)",
        value=2000
    )

    orders_per_day = st.number_input(
        "Orders per day",
        value=5000
    )

with col2:

    items_per_order = st.number_input(
        "Items per order",
        value=2.0
    )

    workers = st.number_input(
        "Number of workers",
        value=20
    )

# ----------------------------
# Analyze Button
# ----------------------------

analyze = st.button("Analyze Warehouse")

# ----------------------------
# Run AI Analysis
# ----------------------------

if analyze and image_bytes_list:

    warehouse_data = {
        "warehouse_size": warehouse_size,
        "orders_per_day": orders_per_day,
        "items_per_order": items_per_order,
        "workers": workers
    }

    with st.spinner("Analyzing warehouse layout..."):

        layouts = []

        for image_bytes in image_bytes_list:
            layout = analyze_layout(image_bytes)
            layouts.append(layout)

        layout_description = "\n\n".join(layouts)

        operations = analyze_operations(
            layout_description,
            warehouse_data
        )

    st.subheader("Layout Analysis")

    st.write(layout_description)

    st.subheader("Operational Insights")

    st.write(operations)

    # ----------------------------
    # Download PDF Report
    # ----------------------------

    pdf = create_pdf_report(layout_description, operations)

    st.download_button(
        label="📄 Download PDF Report",
        data=pdf,
        file_name="warehouse_analysis_report.pdf",
        mime="application/pdf"
    )

elif analyze:

    st.warning("Please upload one or two warehouse layout images or PDFs first.")