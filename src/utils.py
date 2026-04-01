from pdf2image import convert_from_bytes
from io import BytesIO

# -----------------------------
# Convert PDF to image
# -----------------------------
def pdf_to_image_bytes(file_bytes):

    images = convert_from_bytes(file_bytes)

    buffer = BytesIO()

    images[0].save(buffer, format="PNG")

    return buffer.getvalue()


# -----------------------------
# Create PDF report
# -----------------------------
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(layout_analysis, operations_analysis):

    buffer = BytesIO()

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("Warehouse Layout Copilot Report", styles["Title"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Layout Analysis", styles["Heading2"]))
    elements.append(Paragraph(layout_analysis.replace("\n", "<br/>"), styles["BodyText"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Operational Insights", styles["Heading2"]))
    elements.append(Paragraph(operations_analysis.replace("\n", "<br/>"), styles["BodyText"]))

    doc = SimpleDocTemplate(buffer)

    doc.build(elements)

    buffer.seek(0)

    return buffer