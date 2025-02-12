from pathlib import Path
from typing import Optional, Any, List
import numpy as np
import pypdfium2 as pdfium
import PIL
import io

def from_pdf_to_numpy(
        file:  str | Path | bytes,
        scale: float = 300 / 72,
        rgb_mode: bool = True,
        password: Optional[str] = None,
        **kwargs: Any,
    ) -> List[np.ndarray]:
    pdf = pdfium.PdfDocument(file, password=password, autoclose=True)
    return [page.render(scale=adjust_page_size(page.get_width(), page.get_height(), scale), rev_byteorder=rgb_mode, **kwargs).to_numpy() for page in pdf]

def adjust_page_size(width: int, height: int, scale: float) -> float:
    length = max(width, height)
    # allow little bit of tolerance over 842 pixels for A4 at 72 dpi
    return scale if length < 900 else scale * 842 / length

def from_pdf_to_pil(
        file:  str | Path | bytes,
        scale: float = 300 / 72,
        rgb_mode: bool = True,
        password: Optional[str] = None,
        **kwargs: Any,
    ) -> List[PIL.Image.Image]:
    pdf = pdfium.PdfDocument(file, password=password, autoclose=True)
    return [page.render(scale=adjust_page_size(page.get_width(), page.get_height(), scale), rev_byteorder=rgb_mode, **kwargs).to_pil() for page in pdf]

def from_pdf_to_image_bytes(
        file:  str | Path | bytes,
        scale: float = 300 / 72,
        rgb_mode: bool = True,
        password: Optional[str] = None,
        **kwargs: Any,
    ) -> List[bytes]:
    pils = from_pdf_to_pil(file, scale, rgb_mode, password, **kwargs)
    return [image_to_byte_array(pil) for pil in pils]

def image_to_byte_array(image: PIL.Image.Image) -> bytes:
    # BytesIO is a file-like buffer stored in memory
    img_byte_arr = io.BytesIO()
    # image.save expects a file-like as a argument
    image.save(img_byte_arr, format='jpeg')
    # Turn the BytesIO object back into a bytes object
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr
