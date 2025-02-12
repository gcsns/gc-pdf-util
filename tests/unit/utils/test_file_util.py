import sys
import io

sys.path.append('../src')

import tempfile
from unittest.mock import patch, MagicMock
import pytest

from utils.fileUtil import FileUtil

class TestFileUtil:
    @staticmethod
    def create_mock_pdf_writer(num_pages: int) -> MagicMock:
        mock_pdf_writer = MagicMock()
        mock_pdf_writer.pages = [MagicMock() for _ in range(num_pages)]
        return mock_pdf_writer

    @patch('utils.fileUtil.PdfReader')
    @patch('utils.fileUtil.PdfWriter')
    def test_split_pdf_pages_and_save(self, mock_pdf_writer, mock_pdf_reader):
        # Mock PdfReader and PdfWriter instances
        mock_pdf_reader.return_value = MagicMock()
        mock_pdf_writer.return_value = TestFileUtil.create_mock_pdf_writer(num_pages=3)

        # Call the method under test
        result = FileUtil.split_pdf_pages_and_save(b"Mock PDF content")
        # Assertions
        assert isinstance(result, list)

    @pytest.mark.parametrize("file_type, expected_suffix", [('.pdf', '.pdf'), ('.PDF', '.pdf'), ('.txt', '.txt')])
    def test_get_file_suffix(self, file_type, expected_suffix):
        # Call the method under test
        result = FileUtil.get_file_suffix(f"MockFile{file_type}")

        # Assertions
        assert result == expected_suffix

    def test_save_bytes_as_file(self):
        # Create a mock temporary file
        with tempfile.NamedTemporaryFile() as temp_file:
            mock_temp_file_path = temp_file.name
            # Mock NamedTemporaryFile context manager
            with patch('tempfile.NamedTemporaryFile', return_value=temp_file) as mock_named_temp_file:
                # Call the method under test
                result = FileUtil.save_bytes_as_file(b"Mock File Content", '.txt')
                # Assertions
                assert result == mock_temp_file_path

    @staticmethod
    def test_get_page_count_in_pdf():
        # Mocking a valid PDF file as bytes
        VALID_PDF_FILE = io.FileIO('data/ilovepdf_merged.pdf').read()
        assert FileUtil.get_page_count_in_pdf(VALID_PDF_FILE) == 4

    @staticmethod
    def test_convert_to_base64_with_mime():
        assert FileUtil.convert_to_base64_with_mime(b"dummydata", "filename.jpeg") == "data:image/jpeg;base64,ZHVtbXlkYXRh"