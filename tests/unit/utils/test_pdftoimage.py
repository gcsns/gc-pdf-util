import pytest
from unittest.mock import MagicMock, patch
import numpy as np
from PIL import Image
import sys

sys.path.append('../src')
from utils import pdftoimage

@pytest.fixture
def mock_pdf_document_return_value():
    mock_page = MagicMock()
    mock_page.render.return_value.to_numpy.return_value = np.zeros((100, 100, 3))
    mock_page.render.return_value.to_pil.return_value = Image.new('RGB', (100, 100))
    return iter([mock_page])

@patch('utils.pdftoimage.adjust_page_size')
@patch('utils.pdftoimage.pdfium.PdfDocument')
def test_from_pdf_to_numpy(mock_pdf, mock_adjust_page_size, mock_pdf_document_return_value):
    mock_pdf.return_value.__iter__.return_value = mock_pdf_document_return_value
    mock_adjust_page_size.return_value = 1

    file_path = "dummy.pdf"
    result = pdftoimage.from_pdf_to_numpy(file_path)
    
    assert isinstance(result, list)
    assert isinstance(result[0], np.ndarray)
    assert result[0].shape == (100, 100, 3)

@patch('utils.pdftoimage.adjust_page_size')
@patch('utils.pdftoimage.pdfium.PdfDocument')
def test_from_pdf_to_pil(mock_pdf, mock_adjust_page_size, mock_pdf_document_return_value):
    mock_pdf.return_value.__iter__.return_value = mock_pdf_document_return_value
    mock_adjust_page_size.return_value = 1

    file_path = "dummy.pdf"
    result = pdftoimage.from_pdf_to_pil(file_path)
    
    assert isinstance(result, list)
    assert isinstance(result[0], Image.Image)
    assert result[0].size == (100, 100)

@patch('utils.pdftoimage.image_to_byte_array')
@patch('utils.pdftoimage.from_pdf_to_pil')
def test_from_pdf_to_image_bytes(mock_from_pdf_to_pil, mock_image_to_byte_array):
    mock_from_pdf_to_pil.return_value = [b'PIL']
    mock_image_to_byte_array.return_value = b'fake_image_bytes'
    file_path = "dummy.pdf"
    result = pdftoimage.from_pdf_to_image_bytes(file_path)
    
    assert isinstance(result, list)
    assert isinstance(result[0], bytes)
    assert result[0] == b'fake_image_bytes'

def test_image_to_byte_array():
    image = Image.new('RGB', (100, 100))
    result = pdftoimage.image_to_byte_array(image)
    
    assert isinstance(result, bytes)
    # Check the beginning of the JPEG byte stream
    assert result[:2] == b'\xff\xd8'  # JPEG magic number

def test_adjust_page_size():
    result = pdftoimage.adjust_page_size(100, 100, 1)
    assert result == 1

    result = pdftoimage.adjust_page_size(900, 100, 1)
    assert result == pytest.approx(0.936, 0.001)

    result = pdftoimage.adjust_page_size(100, 900, 1)
    assert result == pytest.approx(0.936, 0.001)

    result = pdftoimage.adjust_page_size(900, 900, 1)
    assert result == pytest.approx(0.936, 0.001)

    result = pdftoimage.adjust_page_size(842, 842, 1)
    assert result == 1

    result = pdftoimage.adjust_page_size(900, 842, 1)
    assert result == pytest.approx(0.936, 0.001)

    result = pdftoimage.adjust_page_size(842, 900, 1)
    assert result == pytest.approx(0.936, 0.001)

    result = pdftoimage.adjust_page_size(1000, 1000, 1)
    assert result == pytest.approx(0.842, 0.001)

    result = pdftoimage.adjust_page_size(1000, 1000, 2)
    assert result == pytest.approx(1.684, 0.001)

    result = pdftoimage.adjust_page_size(1000, 1000, 0.5)
    assert result == pytest.approx(0.421, 0.001)

