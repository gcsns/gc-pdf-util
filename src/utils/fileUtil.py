
import os
import io
import tempfile
from pypdf import PdfReader, PdfWriter
import base64
import mimetypes

class FileUtil:

    def save_bytes_as_file(file_bytes: bytes, file_type: str):
        with tempfile.NamedTemporaryFile(suffix=file_type, delete=False) as temp_file:
            temp_file_path = temp_file.name
            temp_file.write(file_bytes)
        return temp_file_path
        
    def split_pdf_pages_and_save(file_bytes: bytes):
        # Create a file-like object from the bytes
        pdf_stream = io.BytesIO(file_bytes)
        
        # Create a PDF reader object
        pdf_reader = PdfReader(pdf_stream)

        # List to store temporary file paths
        temp_file_paths = []
        
        # Iterate through each page of the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Create a new PDF writer object
            pdf_writer = PdfWriter()
            
            # Add the current page to the writer object
            pdf_writer.add_page(pdf_reader.pages[page_num])
            
            # Create a temporary file for the current page
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp_file:
                temp_file_path = temp_file.name
                
                # Write the current page to the temporary file
                with open(temp_file_path, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)
            temp_file_paths.append(temp_file_path)
        return temp_file_paths
    
    def get_file_suffix(filename: str) -> str:
        _, suffix = os.path.splitext(filename)
        return suffix.lower()

    def get_page_count_in_pdf(file: bytes)->int:
        reader = PdfReader(io.BytesIO(file))
        return len(reader.pages)

    def convert_to_base64_with_mime(file: bytes, filename: str):
        # Guess the MIME type of the file based on the filename
        mime_type, _ = mimetypes.guess_type(filename)
        
        if mime_type is None:
            raise ValueError(f"Could not determine the MIME type of the file: {filename}")
        
        # Convert the file bytes to Base64
        base64_encoded = base64.b64encode(file)
        # Convert the Base64 bytes to a string
        base64_string = base64_encoded.decode('utf-8')
        # Add the MIME type prefix
        base64_with_mime = f"data:{mime_type};base64,{base64_string}"
        return base64_with_mime
