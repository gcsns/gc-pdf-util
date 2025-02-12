import io
from pypdf import PdfReader, PdfWriter


class TruncatePagesResult:
    def __init__(self, input_pages: int, output_pages: int, output_pdf: bytes):
        self.input_page_count = input_pages
        self.output_page_count = output_pages
        self.output_pdf = output_pdf


class PdfUtil:
    @staticmethod
    def truncate_pages(
        file_bytes: bytes,
        num_of_pages: int,
    ) -> TruncatePagesResult:
        """
        Truncates the given PDF byte stream to a specified number of pages.

        :param file_bytes: The byte stream of the input PDF file.
        :param num_of_pages: The maximum number of pages to retain in the truncated PDF.
        :return: A TruncatePagesResult containing the original page count,
                 the truncated page count, and the truncated PDF as bytes.
        :raises ValueError: If num_of_pages is less than 1.
        """
        if num_of_pages < 1:
            raise ValueError("The number of pages to retain must be at least 1.")

        input_pdf_stream = io.BytesIO(file_bytes)
        try:
            pdf_reader = PdfReader(input_pdf_stream)
        except Exception as e:
            raise ValueError(f"Unable to read PDF file: {e}")

        pdf_writer = PdfWriter()

        input_pages = len(pdf_reader.pages)  # Count the input pages
        output_pages = min(input_pages, num_of_pages)  # Number of pages to truncate to

        for page_num in range(output_pages):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        output_pdf_stream = io.BytesIO()
        pdf_writer.write(output_pdf_stream)
        output_pdf_stream.seek(0)  # Reset the stream position

        return TruncatePagesResult(
            input_pages, output_pages, output_pdf_stream.getvalue()
        )
