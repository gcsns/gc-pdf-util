import pytest
from io import BytesIO
from pypdf import PdfWriter, PdfReader
import sys

sys.path.append("../src")

from utils.pdf_util import PdfUtil, TruncatePagesResult


# Helper function to create a PDF in memory
def create_test_pdf(num_pages: int) -> bytes:
    pdf_writer = PdfWriter()
    for i in range(num_pages):
        page = PdfWriter().add_blank_page(width=72, height=72)  # Creating a blank page
        pdf_writer.add_page(page)

    pdf_stream = BytesIO()
    pdf_writer.write(pdf_stream)
    return pdf_stream.getvalue()


# Test cases


def test_truncate_more_pages_than_pdf_contains():
    # Given a 5-page PDF, truncate to 10 pages should return only 5
    input_pdf = create_test_pdf(5)
    result = PdfUtil.truncate_pages(input_pdf, 10)

    assert isinstance(result, TruncatePagesResult)
    assert result.input_page_count == 5
    assert result.output_page_count == 5  # Only 5 pages, can't truncate to 10
    truncated_pdf_reader = PdfReader(BytesIO(result.output_pdf))
    assert len(truncated_pdf_reader.pages) == 5


def test_truncate_exact_pages():
    # Given a 5-page PDF, truncate to exactly 5 pages should return all 5 pages
    input_pdf = create_test_pdf(5)
    result = PdfUtil.truncate_pages(input_pdf, 5)

    assert result.input_page_count == 5
    assert result.output_page_count == 5
    truncated_pdf_reader = PdfReader(BytesIO(result.output_pdf))
    assert len(truncated_pdf_reader.pages) == 5


def test_truncate_less_pages_than_pdf_contains():
    # Given a 5-page PDF, truncate to 3 pages should return only 3 pages
    input_pdf = create_test_pdf(5)
    result = PdfUtil.truncate_pages(input_pdf, 3)

    assert result.input_page_count == 5
    assert result.output_page_count == 3  # Only 3 pages should be returned
    truncated_pdf_reader = PdfReader(BytesIO(result.output_pdf))
    assert len(truncated_pdf_reader.pages) == 3


def test_truncate_invalid_page_number():
    # Truncating to less than 1 page should raise a ValueError
    input_pdf = create_test_pdf(5)
    with pytest.raises(
        ValueError, match="The number of pages to retain must be at least 1."
    ):
        PdfUtil.truncate_pages(input_pdf, 0)

    with pytest.raises(
        ValueError, match="The number of pages to retain must be at least 1."
    ):
        PdfUtil.truncate_pages(input_pdf, -5)


def test_truncate_empty_pdf():
    # Testing truncation on an empty PDF (0 pages)
    input_pdf = create_test_pdf(0)
    result = PdfUtil.truncate_pages(input_pdf, 3)

    assert result.input_page_count == 0
    assert result.output_page_count == 0  # Can't truncate to more than 0 pages
    truncated_pdf_reader = PdfReader(BytesIO(result.output_pdf))
    assert len(truncated_pdf_reader.pages) == 0


def test_truncate_invalid_pdf_bytes():
    # Passing invalid bytes should raise a ValueError
    invalid_pdf_bytes = b"Not a PDF"

    with pytest.raises(ValueError, match="Unable to read PDF file"):
        PdfUtil.truncate_pages(invalid_pdf_bytes, 3)
