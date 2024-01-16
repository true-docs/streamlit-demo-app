import filetype
import fitz
from PIL import Image


def is_pdf(data):
    mime = filetype.guess_mime(data)
    return mime is not None and mime == "application/pdf"


def pdf_to_image(data):
    """
    Convert a PDF document to an image,
    taking the first page of the PDF document.
    """
    # Create a PDF document from the in-memory PDF bytes
    # Select the first page (page 0)
    # Convert the page to an image (PNG format)
    pdf_document = fitz.open(stream=data, filetype="pdf")
    first_page = pdf_document.load_page(0)
    pix = first_page.get_pixmap()

    # Build a PIL (Pillow) image from the PyMuPDF pixmap
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Clean up resources
    pdf_document.close()

    return img
