from unittest.mock import patch
from fastapi.testclient import TestClient
import base64

import pytest
import sys

sys.path.append("../src")

from routes.pdf import router

client = TestClient(router)


# Helper function to generate a valid PDF file in bytes (for mocking PDF input)
def create_mock_pdf():
    from io import BytesIO
    from pypdf import PdfWriter

    pdf_writer = PdfWriter()
    pdf_writer.add_blank_page(width=72, height=72)  # Adding a simple blank page

    pdf_bytes = BytesIO()
    pdf_writer.write(pdf_bytes)
    return pdf_bytes.getvalue()


def test_convert_to_images_success():
    with patch("routes.pdf.from_pdf_to_image_bytes") as mock_from_pdf_to_image_bytes:
        mock_from_pdf_to_image_bytes.return_value = [b"fake image data"]
        response = client.post(
            "/pdf/convert-to-images",
            files={"file": ("test.pdf", b"fake pdf data", "application/pdf")},
        )
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["fileName"] == "test-1.jpg"
        # The base64 encoding of "fake image data" is "ZmFrZSBpbWFnZSBkYXRh"
        assert response.json()[0]["content"] == "ZmFrZSBpbWFnZSBkYXRh"


# Test: Successful PDF truncation
def test_truncate_pdf_success():
    mock_pdf = create_mock_pdf()

    # Call the API with the mock PDF and valid number of pages in form data
    response = client.post(
        "/pdf/truncate",
        files={"file": ("test.pdf", mock_pdf, "application/pdf")},
        data={"num_of_pages": "1"},  # num_of_pages is now sent in form data
    )

    # Assert the response is successful
    assert response.status_code == 200
    json_response = response.json()

    # Assert the PDF metadata is returned correctly
    assert json_response["input_page_count"] == 1
    assert json_response["output_page_count"] == 1

    # Check if the base64 content is a valid PDF by decoding and verifying the first few bytes
    pdf_base64 = json_response["pdf_base64"]
    pdf_bytes = base64.b64decode(pdf_base64)

    # Verify the first bytes of the PDF file (PDF files start with '%PDF')
    assert pdf_bytes[:4] == b"%PDF"


# Test: Invalid `num_of_pages` (e.g., less than 1)
def test_truncate_pdf_invalid_num_of_pages():
    with pytest.raises(Exception):
        mock_pdf = create_mock_pdf()

        # Call the API with num_of_pages less than 1 in form data
        response = client.post(
            "/pdf/truncate",
            files={"file": ("test.pdf", mock_pdf, "application/pdf")},
            data={"num_of_pages": "0"},  # Invalid num_of_pages in form data
        )

        # Assert that the response is a 400 Bad Request
        assert response.status_code == 400
        assert response.json() == {
            "detail": "The number of pages to retain must be at least 1."
        }


# Test: Invalid PDF file input
def test_truncate_pdf_invalid_pdf():
    with pytest.raises(Exception):
        invalid_pdf_data = b"This is not a PDF file"

        # Call the API with invalid PDF data
        response = client.post(
            "/pdf/truncate",
            files={"file": ("test.pdf", invalid_pdf_data, "application/pdf")},
            data={"num_of_pages": "1"},  # Valid form data
        )

        # Assert that the response is a 400 Bad Request for invalid PDF
        assert response.status_code == 400
        assert response.json() == {
            "detail": "Unable to read PDF file. Ensure it is a valid PDF."
        }


def test_latex_to_pdf_success():
    with patch("routes.pdf.subprocess.run") as mock_run, patch("builtins.open", new_callable=pytest.mock.mock_open, read_data=b"%PDF") as mock_open:
        mock_run.return_value.returncode = 0
        mock_open.return_value.read.return_value = b"%PDF"

        response = client.post("/pdf/render-latex-pdf", data={"latex_code": "\\documentclass{article}\\begin{document}Hello, world!\\end{document}"})
        
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/pdf"
        assert response.content[:4] == b"%PDF"


def test_latex_to_pdf_failure():
    with patch("routes.pdf.subprocess.run", side_effect=subprocess.CalledProcessError(1, "pdflatex")):
        response = client.post("/pdf/render-latex-pdf", data={"latex_code": "\\invalidLatexCode"})
        
        assert response.status_code == 200
        assert response.json() == {"error": "pdflatex compilation failed"}


def test_recreate_pdf_success():
    mock_pdf = create_mock_pdf()
    with patch("routes.pdf.recreatePdfFunc") as mock_recreate:
        mock_recreate.return_value = {"status": "success", "message": "PDF recreated"}

        response = client.post("/pdf/recreate-pdf", files={"file": ("test.pdf", mock_pdf, "application/pdf")})
        
        assert response.status_code == 200
        assert response.json() == {"status": "success", "message": "PDF recreated"}